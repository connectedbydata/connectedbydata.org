---
layout: default
title: Solutions
subtitle: How could things work instead?
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

{%- assign participation = site.solutions | where:"id", "/solutions/participation" | first -%}
{%- assign organisations = site.solutions | where:"id", "/solutions/organisations" | first -%}
{%- assign people = site.solutions | where:"id", "/solutions/people" | first -%}

{%- capture block2 -%}
  <div class="columns is-gapless">
    {%- include block.html background='mountain' hidden='mobile' -%}
    {%- include block.html background='darker-green' hidden='touch' -%}
    {%- include home-block.html section=participation background='darkest-green' -%}
  </div>
  <div class="columns is-gapless is-mobile is-hidden-tablet">
    {%- include block.html background='darkest-green' -%}
    {%- include block.html background='triangle' -%}
  </div>
  <div class="columns is-gapless">
    {%- include home-block.html section=organisations background='darker-green' -%}
    {%- include block.html background='darkest-green' hidden='touch' -%}
    {%- include block.html background='triangle' hidden='mobile' -%}
  </div>
  <div class="columns is-gapless is-mobile is-hidden-tablet">
    {%- include block.html background='cube' -%}
    {%- include block.html background='dark-green' -%}
  </div>
  <div class="columns is-gapless">
    {%- include block.html background='square' hidden='mobile' -%}
    {%- include home-block.html section=people background='dark-green' -%}
    {%- include block.html background='dark-green' hidden='touch' -%}
  </div>
{%- endcapture -%}
{%- include section.html content=block2 -%}

</article>