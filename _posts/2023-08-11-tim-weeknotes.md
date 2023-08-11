---
layout: post
author: Tim Davies
category: weeknotes
---

## Designing dialogue on beneficial ownership transparency

I’ve [written in weeknotes before](http://connectedbydata.org/weeknotes/2023/01/27/tim-weeknotes) about the somewhat obscure sounding topic of ‘beneficial ownership transparency’. In short, a beneficial owner is someone who ultimately owns, controls or benefits from some asset (like a company, or real estate), even when that asset might be directly owned through some intermediary structure like a company, trust or offshore entity. Over the last decade there have been moves to bring in greater transparency of beneficial ownership, to address issues including tax evasion, money laundering, and abuse of corporate structures to evade responsibility for legal, social or environmental issues. However, exactly how this transparency should be delivered is hotly contested. What data should be public? If data is not public, who should have access? And how can disclosures be published in ways that allow investigators to follow complex ownership structures across borders?

Back in January, I mused on the role that collective, participatory and deliberative processes could play in shaping the future of beneficial ownership transparency. Today I sat down for a few hours co-working with  from the [Centre for Public Data](https://www.centreforpublicdata.org/) to dig deeper into these questions. 

Although my starting point had been thinking about the role of broad public engagement, we quickly identified that, in practice, to give communities a powerful voice in the governance of beneficial ownership data would require an initial focus on the civil society organisations and stakeholders involved in beneficial ownership advocacy. 

In short, because a powerful voice for communities on this relatively technocratic issue is likely to come primarily through civil society advocacy, then it makes sense to first explore the alignment of civil society campaigner positions. Once civil society groups are broadly aligned in their policy asks, then it would make sense of try and pursue a civil-society organised public dialogue that can (a) validate or challenge the details of civil society policy prescriptions; (b) provide evidence in public attitudes towards appropriate access regimes for beneficial ownership information to support advocacy. 

**Initial design notes for a dialogue**

My working assumption is that, whilst many organisation have a shared interest in seeing some form of beneficial ownership transparency, when it comes to the exact details of data access arrangements, there may be different interests and preferences depending on the precise use-case (e.g. investigating particular companies or beneficial owners vs. establishing systemic problems in a countries’ anti-money laundering processes). 

There are at least four dimensions on which arrangements for access to beneficial ownership information could vary:

* **Query mechanism**: Can data be accessed in bulk? Is data only available through requests for individual records? Or, is there a secure query environment that allows analysis without providing direct access to underlying data? 
* **Access control**: Is data published as open data? Is data generally accessible, but under restricted licence conditions? Or is data only available to accredited users?
* **Fields provided**: Is data pseudonymised or anonymised? Are fields used for fuzzy matching of identity provided (e.g. address, date of birth, nationality)? 
* **Accreditation process**: If accreditation to access data is required, who is eligible? Is self-certification of a legitimate interest possible? What is the process to apply? Is accreditation portable across data sources? How long does accreditation take? 

For the first two of these, I think we can reasonable construct a brief matrix of options:

<table>
  <tr>
   <td>
   </td>
   <td><strong>Open</strong>
   </td>
   <td><strong>Licensed access</strong>
   </td>
   <td><strong>Accredited access only</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Bulk access</strong>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Hosted query service</strong>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Request based service</strong>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>

Different stakeholders will find their needs more-or-less served by different positions in this matrix, even before the details of field-level disclosure, or accreditation process are taken into account. For example, a use case that relies on making connections between different datasets is likely to want to see a form of bulk-access, as a request-based service (where information on each company or owner has to be requested one-by-one) is likely to prove prohibitively costly in terms of time. On the other hand, a researcher interested in understanding patterns of ownership, as opposed to individual ownership structures, may be happy to use a hosted query service. 

The [NHS AI Lab dialogue I observed last year](http://connectedbydata.org/blog/2023/02/23/nhs-ai-lab-public-dialogue-data-stewardship) offers a possible template for presenting different data access and governance mechanisms to a group, and talking through both their different variants, and the pros and cons the group see with each option.

If we can use a set of interviews to elaborate the access requirements above, we should be able to prepare background materials to support a meaningful dialogue. 

An ‘expert’ dialogue involving campaigners, journalists, lawyers and technologists could then provide additional testimony and evidence that could be fed into the materials for a public dialogue. 

To balance this, we would also need to make sure we gather and present insight and evidence on the perceived risks and community impacts of these different access regimes: both for the civil society dialogue, and any broader public dialogue. One of the challenges of current debate appears to be that it is often based on perceptions of possible risk, but without naming the particular communities that might be positively or negatively impacted by any particular regime. For example, while at first glance it might look like current problems with trusts enabling opacity of ownership through the Register of Overseas Entities would be solved if all trusts were simply required to publish their beneficial owners (trusts often perceived as a tool of the wealthy and powerful), I know from experience [writing a will as an adoptive parent](https://ridleyandhall.co.uk/how-best-to-make-provision-for-your-adopted-child-in-your-will/), that trusts are also widely used to support/protect potentially vulnerable individuals. 

**General reflections**

We’re going to sound out a few more organisations to see if there is appetite for a deliberative workshop on beneficial ownership transparency access regimes

Regardless, it’s been an interesting thought experiment to start digging deeper into:

1. The interaction between **powerful public voice** and **civil society campaigning **in relatively technical/specialist areas of data;
2. The value in identifying different communities interested in, or affected by, any particular data governance arrangements.