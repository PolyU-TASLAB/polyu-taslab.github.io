(function () {
  var root = document.querySelector(".visitors");
  if (!root) return;

  var svg = root.querySelector(".visitors-map svg");
  var list = root.querySelector(".visitors-list");
  var base = root.dataset.base;
  var site = root.dataset.site;
  var apiKey = root.dataset.key;
  var since = root.dataset.since;
  var cached = [];
  try {
    cached = JSON.parse(root.querySelector(".visitors-data").textContent).stats || [];
  } catch (e) {}

  var GROUPS = { HK: "HMT", MO: "HMT", TW: "HMT" };
  var NAMES = { HMT: "Hong Kong, Macau & Taiwan", CN: "Mainland China" };
  // the 110m map has no polygons for Hong Kong and Macau
  var MAP_ALIAS = { HK: "CN", MO: "CN" };

  function code(row) {
    var id = String(row.id || row.code || "").split("-")[0].toUpperCase();
    return /^[A-Z]{2}$/.test(id) ? id : "";
  }

  function tally(rows, keyFn) {
    var out = {};
    rows.forEach(function (row) {
      var c = code(row);
      if (!c) return;
      var key = keyFn(c);
      out[key] = out[key] || { key: key, name: NAMES[key] || row.name || key, count: 0 };
      out[key].count += Number(row.count) || 0;
    });
    return out;
  }

  // Live counts straight from GoatCounter (read-only key), falling back to the build-time copy.
  function loadRows() {
    if (!site || !apiKey) return Promise.resolve(cached);
    var url = "https://" + site + ".goatcounter.com/api/v0/stats/locations?limit=200" +
      (since ? "&start=" + since + "T00:00:00Z" : "");
    return fetch(url, { headers: { Authorization: "Bearer " + apiKey } })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.json();
      })
      .then(function (data) { return data.stats || []; })
      .catch(function () { return cached; });
  }

  function renderList(byCountry) {
    var ranked = Object.keys(byCountry)
      .map(function (k) { return byCountry[k]; })
      .sort(function (a, b) { return b.count - a.count; });
    if (!ranked.length) {
      list.innerHTML = '<li class="visitors-empty">Visitor statistics will appear here soon.</li>';
      return;
    }
    var max = ranked[0].count;
    list.innerHTML = ranked
      .map(function (r) {
        var pct = Math.max(2, Math.round((r.count / max) * 100));
        return (
          '<li><span class="visitors-name">' + r.name + "</span>" +
          '<span class="visitors-count">' + r.count.toLocaleString("en") + "</span>" +
          '<span class="visitors-bar" aria-hidden="true"><span style="width:' + pct + '%"></span></span></li>'
        );
      })
      .join("");
  }

  function shade(count, max) {
    if (!count) return "#e6e8ec";
    var t = Math.max(0.2, Math.min(1, Math.sqrt(count / max)));
    var lo = [246, 226, 231], hi = [165, 0, 52];
    return "rgb(" + lo.map(function (v, i) { return Math.round(v + (hi[i] - v) * t); }).join(",") + ")";
  }

  function load(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function renderMap(byShape) {
    Promise.all([
      load("https://cdn.jsdelivr.net/npm/d3-array@3"),
      load("https://cdn.jsdelivr.net/npm/topojson-client@3"),
      fetch(base + "countries-110m.json").then(function (r) { return r.json(); }),
    ])
      .then(function (res) {
        return load("https://cdn.jsdelivr.net/npm/d3-geo@3").then(function () { return res[2]; });
      })
      .then(function (topo) {
        var w = 960, h = 480;
        var projection = d3.geoNaturalEarth1().fitSize([w, h], { type: "Sphere" });
        var path = d3.geoPath(projection);
        var max = 0;
        Object.keys(byShape).forEach(function (k) { max = Math.max(max, byShape[k].count); });
        var ns = "http://www.w3.org/2000/svg";
        var sphere = document.createElementNS(ns, "path");
        sphere.setAttribute("class", "visitors-sphere");
        sphere.setAttribute("d", path({ type: "Sphere" }));
        svg.appendChild(sphere);
        topojson.feature(topo, topo.objects.countries).features.forEach(function (f) {
          if (f.properties.name === "Antarctica") return;
          var hit = byShape[f.properties.a2];
          var p = document.createElementNS(ns, "path");
          p.setAttribute("d", path(f));
          p.setAttribute("fill", shade(hit ? hit.count : 0, max));
          var title = document.createElementNS(ns, "title");
          title.textContent = (hit ? hit.name : f.properties.name) + (hit ? ": " + hit.count.toLocaleString("en") : "");
          p.appendChild(title);
          svg.appendChild(p);
        });
      })
      .catch(function () {
        svg.parentNode.classList.add("visitors-map-failed");
      });
  }

  function start() {
    loadRows().then(function (rows) {
      renderList(tally(rows, function (c) { return GROUPS[c] || c; }));
      renderMap(tally(rows, function (c) { return MAP_ALIAS[c] || c; }));
    });
  }

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) {
        io.disconnect();
        start();
      }
    }, { rootMargin: "300px" });
    io.observe(root);
  } else {
    start();
  }
})();
