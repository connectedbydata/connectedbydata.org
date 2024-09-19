---
layout: default
title: Problems
subtitle: What are problems we're trying to solve?
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

{%- assign impact = site.problems | where:"id", "/problems/impact" | first -%}
{%- assign ownership = site.problems | where:"id", "/problems/ownership" | first -%}
{%- assign connected = site.problems | where:"id", "/problems/connected" | first -%}

{%- capture block1 -%}
  <div class="columns is-gapless">
    {%- include home-block.html section=impact background='dark-green' -%}
    {%- include block.html background='rhombus' hidden='mobile' -%}
    {%- include block.html background='darker-green' hidden='touch' -%}
  </div>
  <div class="columns is-gapless is-mobile is-hidden-tablet">
    {%- include block.html background='imperfect-circle' -%}
    {%- include block.html background='dark-green' -%}
  </div>
  <div class="columns is-gapless">
    {%- include block.html background='imperfect-circle' hidden='mobile' -%}
    {%- include block.html background='dark-green' hidden='touch' -%}
    {%- include home-block.html section=ownership background='darker-green' -%}
  </div>
  <div class="columns is-gapless is-mobile is-hidden-tablet">
    {%- include block.html background='darkest-green' -%}
    {%- include block.html background='medium-dots' -%}
  </div>
  <div class="columns is-gapless">
    {%- include home-block.html section=connected background='darkest-green' -%}
    {%- include block.html background='darkest-green' hidden='touch' -%}
    {%- include block.html background='medium-dots' hidden='mobile' -%}
  </div>
{%- endcapture -%}
{%- include section.html content=block1 -%}

</article>