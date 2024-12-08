import os
import subprocess
import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path
from datetime import date, datetime
from rich import print
from diskcache import Cache
from serpapi import GoogleSearch


# cache for time-consuming network requests
cache = Cache("./_cite/.cache")


# clear expired items from cache
cache.expire()


def log_cache(func):
    """
    decorator to use around memoized function to log if cached or or not
    """

    def wrap(*args):
        key = func.__cache_key__(*args)
        if key in cache:
            log(" (from cache)", level="INFO", newline=False)
        return func(*args)

    return wrap


def log(message="\n--------------------\n", indent=0, level="", newline=True):
    """
    log to terminal, color determined by indent and level
    """

    palette = {
        0: "[orange1]",
        1: "[salmon1]",
        2: "[violet]",
        3: "[sky_blue1]",
        "ERROR": "[white on #F43F5E]",
        "WARNING": "[black on #EAB308]",
        "SUCCESS": "[black on #10B981]",
        "INFO": "[grey70]",
    }
    color = get_safe(palette, level, "") or get_safe(
        palette, indent, "") or "[white]"
    if newline:
        print()
    print(indent * "    " + color + str(message) + "[/]", end="", flush=True)


def label(entry):
    """
    get "label" of dict entry (for logging purposes)
    """

    return str(list(entry.keys())[0]) + ": " + str(list(entry.values())[0])


def get_safe(item, path, default=None):
    """
    safely access value in nested lists/dicts
    """

    for part in str(path).split("."):
        try:
            part = int(part)
        except ValueError:
            part = part
        try:
            item = item[part]
        except (KeyError, IndexError, AttributeError, TypeError):
            return default
    return item


def list_of_dicts(data):
    """
    check if data is list of dicts
    """

    return isinstance(data, list) and all(isinstance(entry, dict) for entry in data)


def format_date(_date):
    """
    format date as YYYY-MM-DD, or no date if malformed
    """

    if isinstance(_date, int):
        return datetime.fromtimestamp(_date // 1000.0).strftime("%Y-%m-%d")
    if isinstance(_date, (date, datetime)):
        return _date.strftime("%Y-%m-%d")
    try:
        return datetime.strptime(_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except Exception:
        return ""


def load_data(path):
    """
    read data from yaml or json file
    """

    # convert to path object
    path = Path(path)

    # check if file exists
    if not path.is_file():
        raise Exception("Can't find file")

    # try to open file
    try:
        file = open(path, encoding="utf8")
    except Exception as e:
        raise Exception(e or "Can't open file")

    # try to parse as yaml
    try:
        with file:
            data = yaml.load(file, Loader=SafeLoader)
    except Exception:
        raise Exception("Can't parse file. Make sure it's valid YAML.")

    # if no errors, return data
    return data


def save_data(path, data):
    """
    write data to yaml file
    """

    # convert to path object
    path = Path(path)

    # try to open file
    try:
        file = open(path, mode="w")
    except Exception:
        raise Exception("Can't open file for writing")

    # prevent yaml anchors/aliases (pointers)
    yaml.Dumper.ignore_aliases = lambda *args: True

    # try to save data as yaml
    try:
        with file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
    except Exception:
        raise Exception("Can't save YAML to file")

    # write warning note to top of file
    note = "# DO NOT EDIT, GENERATED AUTOMATICALLY"
    try:
        with open(path, "r") as file:
            data = file.read()
        with open(path, "w") as file:
            file.write(f"{note}\n\n{data}")
    except Exception:
        raise Exception("Can't write to file")


@log_cache
@cache.memoize(name="manubot", expire=90 * (60 * 60 * 24))
def cite_with_manubot(_id):
    """
    generate citation data for source id with Manubot
    """

    # run Manubot
    try:
        commands = ["manubot", "cite", _id, "--log-level=WARNING"]
        output = subprocess.Popen(
            commands, stdout=subprocess.PIPE).communicate()
    except Exception as e:
        log(e, 3)
        raise Exception("Manubot could not generate citation")

    # parse results as json
    try:
        manubot = json.loads(output[0])[0]
    except Exception:
        raise Exception("Couldn't parse Manubot response")

    # new citation with only needed info
    citation = {}

    # original id
    citation["id"] = _id

    # title
    citation["title"] = get_safe(manubot, "title", "").strip()

    # authors
    citation["authors"] = []
    for author in get_safe(manubot, "author", {}):
        given = get_safe(author, "given", "").strip()
        family = get_safe(author, "family", "").strip()
        if given or family:
            citation["authors"].append(" ".join([given, family]))

    # publisher
    container = get_safe(manubot, "container-title", "").strip()
    collection = get_safe(manubot, "collection-title", "").strip()
    publisher = get_safe(manubot, "publisher", "").strip()
    citation["publisher"] = container or publisher or collection or ""

    # extract date part
    def date_part(citation, index):
        try:
            return citation["issued"]["date-parts"][0][index]
        except (KeyError, IndexError, TypeError):
            return ""

    # date
    year = date_part(manubot, 0)
    if year:
        # fallbacks for month and day
        month = date_part(manubot, 1) or "1"
        day = date_part(manubot, 2) or "1"
        citation["date"] = format_date(f"{year}-{month}-{day}")
    else:
        # if no year, consider date missing data
        citation["date"] = ""

    # link
    citation["link"] = get_safe(manubot, "URL", "").strip()

    # return citation data
    return citation


def main(entry):
    """
    receives single list entry from google-scholar data file
    returns list of sources to cite
    """

    # get api key (serp api key to access google scholar)
    # api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY", "")
    api_key = "e1f7fef6016b0907f03d17bc1acdd7bf7eaabb8c264dec674fd3d5b01bdbecf8"
    print(api_key)
    if not api_key:
        raise Exception('No "GOOGLE_SCHOLAR_API_KEY" env var')

    # serp api properties
    params = {
        "engine": "google_scholar_author",
        "api_key": api_key,
        "num": 100,  # max allowed
    }

    # get id from entry
    # _id = get_safe(entry, "gsid", "")
    _id = "N-AFqt8AAAAJ"
    if not _id:
        raise Exception('No "gsid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        params["author_id"] = _id
        return get_safe(GoogleSearch(params).get_dict(), "articles", [])

    response = query(_id)

    # list of sources to return
    sources = []

    # go through response and format sources
    for work in response:
        # create source
        year = get_safe(work, "year", "")
        source = {
            "id": get_safe(work, "citation_id", ""),
            # api does not provide Manubot-citeable id, so keep citation details
            "title": get_safe(work, "title", ""),
            "authors": list(map(str.strip, get_safe(work, "authors", "").split(","))),
            "publisher": get_safe(work, "publication", ""),
            "date": (year + "-01-01") if year else "",
            "link": get_safe(work, "link", ""),
        }

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources


# error flag
error = False

# output citations file
output_file = "_data/citations.yaml"


log()

log("Compiling sources")

# compiled list of sources
sources = []

# in-order list of plugins to run
plugins = ["google-scholar", "pubmed", "orcid", "sources"]
# plugins = ["google-scholar"]


# loop through plugins
for plugin in plugins:
    # convert into path object
    plugin = Path(f"plugins/{plugin}.py")

    log(f"Running {plugin.stem} plugin")

    # get all data files to process with current plugin
    files = Path.cwd().glob(f"_data/{plugin.stem}*.*")
    files = list(filter(lambda p: p.suffix in [
                 ".yaml", ".yml", ".json"], files))

    log(f"Found {len(files)} {plugin.stem}* data file(s)", 1)

    # loop through data files
    for file in files:
        log(f"Processing data file {file.name}", 1)

        # load data from file
        try:
            data = load_data(file)
            # check if file in correct format
            if not list_of_dicts(data):
                raise Exception("File not a list of dicts")
        except Exception as e:
            log(e, 2, "ERROR")
            error = True
            continue

        # loop through data entries
        for index, entry in enumerate(data):
            log(f"Processing entry {index + 1} of {len(data)}, {label(entry)}", 2)

            # run plugin on data entry to expand into multiple sources
            try:
                expanded = import_module(f"plugins.{plugin.stem}").main(entry)
                # check that plugin returned correct format
                if not list_of_dicts(expanded):
                    raise Exception("Plugin didn't return list of dicts")
            # catch any plugin error
            except Exception as e:
                # log detailed pre-formatted/colored trace
                print(traceback.format_exc())
                # log high-level error
                log(e, 3, "ERROR")
                error = True
                continue

            # loop through sources
            for source in expanded:
                if plugin.stem != "sources":
                    log(label(source), 3)

                # include meta info about source
                source["plugin"] = plugin.name
                source["file"] = file.name

                # add source to compiled list
                sources.append(source)

            if plugin.stem != "sources":
                log(f"{len(expanded)} source(s)", 3)


log("Merging sources by id")

# merge sources with matching (non-blank) ids
for a in range(0, len(sources)):
    a_id = get_safe(sources, f"{a}.id", "")
    if not a_id:
        continue
    for b in range(a + 1, len(sources)):
        b_id = get_safe(sources, f"{b}.id", "")
        if b_id == a_id:
            log(f"Found duplicate {b_id}", 2)
            sources[a].update(sources[b])
            sources[b] = {}
sources = [entry for entry in sources if entry]


log(f"{len(sources)} total source(s) to cite")


log()

log("Generating citations")

# list of new citations
citations = []
