---
layout: post
author: Tim Davies
category: weeknotes
---

## Weeknotes

Sharing updates from UKGovCamp, plus lots of projects kicking into gear this week as 2025 gets into full swing!

## UK Gov Camp 2025

I'm heading back from a day at UKGovCamp - the annual unconference of public sector digital folk that has just turned 18. I've grown up with GovCamp, attending I suspect at least ten editions of the event of the years in a range of guises working on digital youth work, open government data, data standardisation and public engagement - so as well as being a lovely opportunity to catch up with old friends, I find I leave with a mix of new ideas and a challenge to my thinking, and wanting to link out to the archives and re-surface some past thoughts that might be useful to future directions. So - here go notes in that spirit.

### To err is human

I started the day in a session on 'Error rates and data quality' pitched around the growing demand for 'clean data' to feed into AI projects. However, as the session explored, the idea of perfect clean data is a pipe-dream in most public services (and indeed, most contexts in general). Data always has a history and context (c.f. [Raw Data is an oxymoron](https://direct.mit.edu/books/edited-volume/3992/Raw-Data-Is-an-Oxymoron) book and [paper where Mark Frank and I riffed on this for 2013 Web Science Conference](https://dl.acm.org/doi/10.1145/2464464.2464472)) and preparing data for re-use outside that context is non-trivial. I was left thinking about two practical interventions:

1. **Explore methods for interdisciplinary data quality mapping**. For example, I asked if anyone had examples of workshop processes that invite teams to tell the story of their data collection and processing, and that can be used to map out the different points at which data quality issues might occur. I'm imagining flip-chart, post-it-note based processes that invite thinking about data quality across a set of data flows, or within a mapped out data ecosystem. It seems to me that, if data quality is only seen through a metric, rather than also through narratives, we'll miss opportunities to understand where quality and equality connect, and to work out the human processes and trade-offs involved in seeking reduced error or improved quality. In particular, if we accept that 100% data quality (whatever the metric used) will often be hard to achieve, then it really matters that we can explain whether the 5% or 10% of error disproportionately affects a particular group.

2. **Represent data honestly**. I've recently been back in the weeds of modelling Beneficial Ownership Data, doing some work on the [Open Ownership Beneficial Ownership Data Standard (BODS)](https://standard.openownership.org/) around questions on representing the interests (e.g. shareholding, directorships, other forms of control) that connect individuals and companies. The BODS data model is rooted in the idea that it is a collection of statements about the world: it does not record facts (X owns Y), but rather than (at time T, Z made the statement that X holds shares in Y). This can feel like complexity, but it's also important to honestly represent the world, and is intended to signal to users of the data that they have work to do in order to take an opinionated stance on how far they want to trust claims, and how they might reconcile competing claims about the world.

Loading data into data lakes, or preparing data for processing in AI systems, often flattens out the kinds of signals I tried to embed within the structural model of BODS, but I was left wondering if we need to have more discussion over places we can signal more truthful descriptions, not just in meta-data, but hinting at the histories of given fields by replacing, for example, the column heading 'Postcode with 'Reported Postcode' or 'Verified Postcode'. This might seem like a small step, but when our data is going to travel far from the context it was collected with, we perhaps need our column and variable names to more truthfully report what the data is. 

### AI in Local Government

The next session I went to was a quickfire pre-lunch discussion on 'Uses of AI in (local) government, including parliaments role' mostly involving some small group discussions.

I did point to [the write-up of our research for the Local Government Associations' explainer series on AI](https://connectedbydata.org/projects/2023-lga-brickwal-ai-explainer-videos) which drew quite heavily on a brainstorming session at last year's GovCamp. In that, we offer a brief taxonomy of local government AI use, seeking (non-exhaustively) to focus less on particular kinds of AI, and more on the tasks it might be drawn upon for - as well as providing some suggested scrutiny questions for councillors or officers to use when exploring uses of AI. 

One of the interesting discussions in this session was around the pace of change. In [the taxonomy here](https://connectedbydata.org/blog/2024/10/07/local-gov-ai-scripts) I had a go at indicating which uses I thought it would be easy to find live examples of in practice in mid-2024. I suspect that will already have changed quite a bit - and this pace of change does raises interesting engagement and governance challenges. 

### The National Data Library

It was in the Labour Manifesto. There's a team working on developing it. But there still seem to be a lot of questions over what the National Data Library is. Building on a proliferation of alleiterative points beginning with P, there might be a wider write-up of the session coming soon, but I wanted to capture a couple of particular reflections.

1. **Libraries and literacy**. One participant made the key point that the history of libraries is as much about literacy as providing access to books. From the perspective of public engagement in data governance, this feels to me like a productive build on the chosen 'library' metaphor for the NDL. A library that has within its remit building public sector, and public, literacies around data, is laying the groundwork for more informed and inclusive processes of data governance. 

2. **Portals and people**. A few years ago I worked on a piece for the Open Data Institute that I resurface every-so-often, [exploring the history of data portals, and the potential to rethink portals as enablers of civic engagement](https://dataportals.pubpub.org/). It was good to hear some of the ideas we explored in that work mirrored in descriptions of the upcoming London data library: focussed on facilitating connections between people and data as an active process, rather than just cataloguing data on virtual shelves. 

### Are we digita NIMBYs? 

The fourth session I went to threw down the challenge: has the GovCamp crowd become blockers of needed digital reform? Reflecting on the 'AI eye-roll' they have encountered when trying to promote AI-driven government reforms, the person who pitched the session questioned whether positive digital reforms were being held back by unjustified fears or resistance. A rich discussion followed, noting that with hindsight we (as a GovCamp community) should perhaps have been less boosterish about earlier web and social media technologies given what we know now - and that some of the hesitancy about AI proceeding at pace is perhaps well founded in experience of quick benefits, but slower-burn harms in past waves of technology. At the same time, we explored (though perhaps not in these words) the impacts of austerity, and a receeding wave of digital government that has left those still inside the system working to protect reforms rather than push forward a new wave. 

I was particularly struck by the need to better understand and bridge the cultural context of those in AI firms, dealing with the 'intoxicating' sense of power and progress - and those at the coal-face of public service, often dealing with the fatique of keeping systems going under wave after wave of crisis and cuts.

I did find I had a particularly strong reaction to the claim at one point made that surely it was unquestionably good to be 'Saving social workers 60% of their time spent on paperwork'. I find this problematic on a number of levels, not least that the time completing paperwork is often **the work** of reflecting on and making judgement calls about the lives of children or families. As [Bianca Wylie](https://medium.com/@biancawylie/automating-summation-on-ai-and-holding-responsibility-in-relationships-642f9f79534c) has written of the process of writing up workshops, automation doesn't speed up the task - it radically alters it. Refelecting on my own experience spending hours sitting with social workers, talking openly through difficult parts of my own life for the social worker to prepare a 'Prospective Adopters Report' for our application to be approved as adoptive parents, I wonder how this relational process would have been changed if the conversation was recorded and transcribed automatically, rather than trusting the judgement of the social worker to decide what is right to report on or not: filtering the conversation at source. We should remember that there are many cases where the paper work is the work. 

One participant commented, to nods from the room, how problematic it was that Sundar Pichai once talked about getting AI to order his child's birthday present. Yet, getting AI to write a child protection report, when the state is acting in a parental capacity, raises less hackles at first because its less likely there is lived experience of the frontlines of social work in the room. 

This is not to say that there are no places for AI automation, and that over-pressured workers would not initially embrace something promising time savings: but the narrative that lumps together automating paperwork from incoming customer service requests, with automating elements of the states corporate parenting, is one we should be very cautious about. 

### Book Camp

I rounded off the day in a lovely session sharing with a group sharing reflections on our reading. Having had little access to my books this year (all in storage while we complete house eco-retrofit), it was great to get some new book recommendations, and reflect on different reading practices.

### Cordidoor camp

As always, one of the best parts of GovCamp is 'coridoor camp' - the people you run into in the hallways. Many of those conversations were really useful for thinking about how we can better make the case for, and overcome barriers to, embedding participatory practice more in the accelerating roll-out of digital tools. 

## Other bits from the week

### AI & Green Party

On Monday it was great to see the AI Policy that I worked on with colleagues in the Green Party, and that was passed at conference last year, [providing the basis for Green Co-Leader Adrian Ramsay MP's response to the Government's AI Action Plan](https://greenparty.org.uk/2025/01/13/there-is-a-green-elephant-in-the-room-with-governments-ai-plans/) with a strong call that the use of AI be *"driven by the voices of those most affected by this technology development and deployment"*.

And on Tuesday, as part of the member-driven 'Policy Fest' I chaired a fantastic discussion bringing together different expert voices from the Green Party of England and Wales membership to talk about future directions for AI-focussed work: from exploring the links between policies on AI and Health, building on trade union and workers rights policies, and better supporting local councillors to provide scrutiny of decision making about AI. 

I really value the deliberative spirit of Green Party policy meetings: people come with a wide range of backgrounds and experiences - from those working in-depth on AI policy issues day-to-day, to interested amateurs with particular areas of fear, focus or interest, through to retirees with decades of experience in technology or policy, but just finding their way in thinking about the latest wave of AI. Even though opinions varied as to the risks and opportunities posed by AI, I felt there was a spirit of constructure exploration and inclusive listening in the group that made for a rich conversation.

### Participatory AI Research & Practice Symposium

Last week also involved some intense work preparing for the Participatory AI Research and Practice Symposium taking place online (30th Jan) and in Paris (8th Feb) alongside the AI Action Summit.

We've got the [agenda online](https://pairs25.notion.site/) (thanks to a bit of LLM-assisted Google Apps Script wrangling) and registration open and promotion out. It's been great to work with Meg Young of Data & Society, and Pierre Noro at SciencesPo on advancing the practicalities of it all - and I'm incredibly greatful for their support. 

I've also been working on plans for a session on 11th Feb as part of the AI Fringe Hub in Paris, and thinking about how we make the most of all the assembled participatory practice thinkers and doers on the 8th.

### Mapping Participatory Digital Governance

I kicked off interviews this week for our project with the Open Government Partnership on Mapping Participatory Digital Governance. It was great to learn about, and be reminded of, fantastic projects in Eastern Europe, Nigeria and Brazil that are seeking to bring civil society and citizen voices closer to digital policy and practice - and I've lots of new lines of inquiry to explore. More on this one soon. 

### Public Voices in AI: Exploring Adoption of Best Practice

I joined a workshop run by Mhairi Aitkin from the Turing Institute as part of Public Voices in AI work developing tools to support people commissioning or delivering participatory initiatives on AI. It was useful to see the results of the mapping the PVAI team have carried out of existing participatory excercises, and a good reminder to loop back somepoint soon to our [somewhat dormant case study work](https://connectedbydata.org/cases).

We also worked on some planning for the final sessions of our Public Voices in AI People's Advisory Panel, before PVAI formally wraps up at the end of March.
