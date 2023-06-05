---
layout: post
title: How can the Global Data Barometer support action on Data Values?
author: Tim Davies
category: blog
projects:
  - Measuring Data Values Around the World
---

*This is the second post in a series produced as part of the analysis for the [Measuring Data Values Around the World](https://connectedbydata.org/projects/2023-measuring-data-values) project.*

We have previously scoped out how existing [primary data collected from the Global Data Barometer might map to the Data Values framework](https://connectedbydata.org/blog/2023/06/03/what-can-barometer-tell-data-values). As a multi-dimensional composite index, the Global Data Barometer is based on both primary and secondary data sources. 

In this post, we consider if there are elements of data values measurement which could be addressed by drawing on existing secondary indicators or by incorporating additional secondary data sources. These could feed into future iterations of the GDB, or be used in Data Values measurement products, tools or analysis based partially on the GDB. 

<!--more-->

For inclusion in the GDB secondary data had to pass a number of tests:

* **Broad global coverage**. Where secondary indicators do not cover every country covered by the Barometer, a reasonable method for estimating or imputing missing data should be available. 
* **Robust data collection method.** There should be a clearly documented methodology for the indicator(s) and evidence to show how data quality is assured.
* **Sensitivity to differences between countries**. All indicators are re-scored on a 1 - 100 scale for inclusion in the GDB. There should be a clear approach to do this which ensures differences in fact between countries are reflected by reasonable changes in the indicator score. 
* **Stability**. We should be reasonably confident that the indicator will continue to be produced, and updated, without disruptive methodological changes, in future years, to support time-series analysis of the GDB. 
* **Available and openly licensed data.** The indicator data should be easy to access, and should be provided under terms that permit its inclusion, and ideally redistribution, as part of the GDB. 

In the table below we’ve identified a number of potential secondary data sources and indicators that could either feed into specific **Data Values** **country insight tools (DVT)** that draw on the GDB, or that could be used to expand how far **future editions (2ndEd)** of the GDB address data values  

[In this notebook we’ve tested](https://colab.research.google.com/drive/1LZWHzEPnFjho6Am-td0MYLWKwBcBWNiq) our ability to gather and draw on this data.

Following assessments, we have made use of the following datasets in the working prototype of a data values country insight tool:

<table>
  <tr>
   <td><strong>Source</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Potential use</strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://unstats.un.org/sdgs/dataportal">SDG Indicator Database</a> (<a href="https://colab.research.google.com/drive/1LZWHzEPnFjho6Am-td0MYLWKwBcBWNiq#scrollTo=y0N7En6Q9gVx&line=15&uniqifier=1">Notebook</a>)
   </td>
   <td>Contains SDG data reported by countries, and can be used to identify the degree of disaggregation reported on key indicators
   </td>
   <td><strong>DVT & 2ndEd: </strong>Proxy to identify cases where countries may be collecting disaggregated, and intersectional, data (Manifesto 1 > Outcome metric) 
   </td>
  </tr>
  <tr>
   <td><a href="https://www.worldbank.org/en/programs/statistical-performance-indicators/Framework">Statistical Performance Indicators</a> (<a href="https://colab.research.google.com/drive/1LZWHzEPnFjho6Am-td0MYLWKwBcBWNiq#scrollTo=Uj8rfFEitjTp">Notebook</a>)
   </td>
   <td>Built from secondary indicators to address data infrastructure, sources, products, services and use. Certain valuable fields (e.g. funding and investment in data) are defined, but not populated due to current data gaps. Future editions of SPI may include this data.
   </td>
   <td><strong>DVT: </strong>Provides evidence on quality of statistical infrastructure (Manifesto 1 > Foundations) and availability of data services (Manifesto 4 > Outcomes)
   </td>
  </tr>
  <tr>
   <td><a href="https://www.idea.int/data-tools/tools/global-state-democracy-indices">Global State of Democracy Indices</a> (<a href="https://colab.research.google.com/drive/1LZWHzEPnFjho6Am-td0MYLWKwBcBWNiq#scrollTo=O4HLeUKjo2pC">Notebook</a>)
   </td>
   <td>Contains constructs based on the Varieties of Democracy survey that address consultation practice, and openness of government to consultation inputs.
   </td>
   <td><strong>DVT:</strong> Evidence of general (non data-specific) consultation frameworks. (Manifesto 1 > Foundations); <strong>2ndEd: </strong>Governance or Capability pillar (considering ‘public participation around data’ as a capability to be measured) 
   </td>
  </tr>
  <tr>
   <td><a href="https://odin.opendatawatch.com/">Open Data Inventory</a> (<a href="https://colab.research.google.com/drive/1LZWHzEPnFjho6Am-td0MYLWKwBcBWNiq#scrollTo=82nXI2O_wPuj&line=1&uniqifier=1">Notebook</a>)
   </td>
   <td>Based on assessment of availability of key datasets from national statistical offices, including measures of coverage and disaggregation (customised to relevant disaggregations or coverage criteria for each indicator)
   </td>
   <td><strong>DVT & 2ndEd: </strong>Proxy to identify cases where countries may be collecting disaggregated, and intersectional, data (Manifesto 1 > Outcome metric) <strong> </strong>
   </td>
  </tr>
</table>

We also explored potential further sources, [as documented in the notebook](https://colab.research.google.com/drive/1LZWHzEPnFjho6Am-td0MYLWKwBcBWNiq), but these do not feature in the prototype or suggestions for future GDB secondary data.

The next post in this series will document the prototype tool we've created to explore use of this secondary data alongside data collected by the Barometer. 