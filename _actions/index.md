---
layout: default
title: Actions
subtitle: How can we make these changes happen?
---
<article>

{%- capture header -%}
  {%- capture breadcrumbs -%}
    <li><a href="/#{{ page.collection }}">{{ page.collection | capitalize }}</a></li>
  {%- endcapture -%}
  {%- include breadcrumbs.html items=breadcrumbs -%}
  <h1 class="title is-1 is-size-3-mobile">{{ page.title }}</h1>
  <p class="subtitle is-3 is-size-5-mobile">{{ page.subtitle }}</p>
{%- endcapture -%}
{%- include header.html content=header -%}

{%- assign narrative = site.actions | where:"id", "/actions/narrative" | first -%}
{%- assign practice = site.actions | where:"id", "/actions/practice" | first -%}
{%- assign policy = site.actions | where:"id", "/actions/policy" | first -%}

{%- capture block3 -%}
  <div class="columns is-gapless">
    {%- include home-block.html section=narrative background='darkest-green' -%}
    {%- include block.html background='small-triangles' hidden='mobile' -%}
    {%- include block.html background='darkest-green' hidden='touch' -%}
  </div>
  <div class="columns is-gapless is-mobile is-hidden-tablet">
    {%- include block.html background='small-triangles' -%}
    {%- include block.html background='darkest-green' -%}
  </div>
  <div class="columns is-gapless">
    {%- include block.html background='darker-green' hidden='touch' -%}
    {%- include block.html background='stairs' hidden='mobile' -%}
    {%- include home-block.html section=practice background='dark-green' -%}
  </div>
  <div class="columns is-gapless is-mobile is-hidden-tablet">
    {%- include block.html background='darker-green' -%}
    {%- include block.html background='stairs' -%}
  </div>
  <div class="columns is-gapless">
    {%- include home-block.html section=policy background='darker-green' -%}
    {%- include block.html background='circles' hidden='mobile' -%}
    {%- include block.html background='dark-green' hidden='touch' -%}
  </div>
{%- endcapture -%}
{%- include section.html content=block3 -%}

</article>