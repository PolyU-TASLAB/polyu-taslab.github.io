---
title: Contact
nav:
  order: 6
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

<!-- Add content here.  -->

{%
  include button.html
  type="email"
  text="tas.lab.polyu@gmail.com"
  link="tas.lab.polyu@gmail.com"
%}
{%
  include button.html
  type="phone"
  text="(852) 5566 2851"
  link="+852 55662851"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/Aj8Zj2xQ8KzHSRtr9"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/AboutPolyU_Campus3.png"
  caption=" "
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/AboutPolyU_Campus5.jpg"
  caption=" "
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}

{% endcapture %}

{% capture col2 %}

{% endcapture %}

{% capture col3 %}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
