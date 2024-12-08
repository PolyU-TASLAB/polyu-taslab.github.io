---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

<!-- Include a large landscape photo below the TEAM title -->

![Team Photo](image/team/team.jpg)

#### Faculty (Principal Investigator)
{% include list_pi.html data="members" component="portrait_pi" filters="role == 'pi'"  %}
#### Postdoctoral Fellows
{% include list_students.html data="members" component="portrait_students" filters="role == 'postdoc'" %}
#### Ph.D. Students
{% include list_students.html data="members" component="portrait_students" filters="role == 'phd'" %}
#### M.S./MPhil Students
{% include list_students.html data="members" component="portrait_students" filters="role == 'ms'" %}
#### Research/Project Assistant
{% include list_students.html data="members" component="portrait_students" filters="role == 'ra'" %}
#### Undergraduate Students
{% include list_students.html data="members" component="portrait_students" filters="role == 'under'" %}
#### Visiting Scholar/Students
{% include list_students.html data="members" component="portrait_students" filters="role == 'visiting'" %}
#### Alumni

