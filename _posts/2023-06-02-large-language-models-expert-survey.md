---
layout: post
title: "The potential and pitfalls of text-generating Large Language Models (LLM) in expert surveys"
author: Tim Davies
category: blog
projects:
  - Measuring Data Values Around the World
---

As part of our project exploring how the [Global Data Barometer](https://globaldatabarometer.org/) might be used to provide insights and metrics for measurement against the [Data Values framework](https://www.data4sdgs.org/datavaluesproject/manifesto-demanding-fair-data-future), I’ve been looking into how Large Language Models (LLMs) like ChatGPT might impact upon the methodology of expert survey studies like the Barometer.

This post contains some initial notes from this exploration.

<!--more-->

[Disclaimer: I was the initial project director of the Global Data Barometer, but do not work for the GDB any more, and my comments here do not represent any positions of the Barometer project.]

## How do expert survey studies work?

In a multi-country expert survey like the Barometer, researchers are hired to complete a standard questionnaire through a mix of desk research and primary research with key informants. Generally, researchers are based in, or have in-depth experience of, the countries they are researching, and are asked to respond to the questionnaire with structured responses to closed questions, and to provide written justifications and source links to back up each answer.

Various levels of review take place to quality control data, often though in practice reliant on checking that closed question answers are supported by the written justifications given. Language barriers, the complexity of interpreting source materials from different national contexts, and time constraints, mean that reviews do not necessarily double-check every claim made in a researcher's answer. The cost of paying researchers means that the project uses one researcher for each country.

## What are text generating LLMs?

LLMs like ChatGPT are essentially predictive text engines. Given a prompt, an LLM generates prose (or code, or data) by predicting the most ‘credible’ words that come next in a sentence (or string of any sort). [This blog post from Stephn Wolfram provides a detailed and illuminating explanation of their inner working](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/). LLMs produce surprisingly effective results by using machine-learning models trained on vast quantities of existing text, sourced primarily from online publications.

LLMs were originally developed to support activities like speech recognition (working out the most credible next word in the sentence is helpful to a machine not sure which word it just ‘heard’), but when presented in chat bot form, have found a far wider range of applications.

However, it is important to note that LLMs are not thinking, nor do they have any concept of truth. The ability of these tools to generate ‘true’ sentences is because in many cases a true sentence is the most credible according to the model. But these tools are also prone to generate falsehoods, or fictions (sometimes referred to as hallucinations) and have no way of distinguishing between true or false statements, nor of explaining or sourcing the claims they generate.

## Why LLMs undermine expert surveys as we know them

I ran brief tests using a ChatGPT plugin on Google Sheets to respond to a set of Global Data Barometer questions with LLM responses.

I gave the following prompt:

> “You are a researcher tasked with carrying out critical analysis of country performance against a set of metrics. You are sceptical and cautious about the judgements you make. I am going to ask you a question about The United Kingdom. To what extent do relevant laws, regulations, policies, and guidance provide a comprehensive framework for data sharing? Start your answer with ‘No framework exists’ or ‘A framework exists but lacks full force of law’ or ‘A framework exists and has the force of law’. Then provide 2 – 3 lines of justification for your answer.

And ChatGPT returns a confident answer:

> “A framework exists and has the force of law. The United Kingdom has established a comprehensive framework for data sharing through various laws, regulations, policies, and guidance. The General Data Protection Regulation (GDPR) implemented in 2018 sets the legal basis for data sharing, ensuring that personal data is processed lawfully and securely. Additionally, the Data Protection Act 2018 further supplements the GDPR and provides specific provisions for data sharing. These legislative measures, along with accompanying guidelines from the Information Commissioner's Office (ICO), create a robust framework that governs data sharing practices in the United Kingdom.”

Repeating the prompt for a different country (Malaysia) we get:

> “A framework exists but lacks full force of law. Malaysia has made efforts to establish a framework for data sharing through various laws, regulations, policies, and guidance. The Personal Data Protection Act (PDPA) of 2010 provides a legal framework for the protection of personal data, including provisions for data sharing. Additionally, the Malaysian Administrative Modernisation and Management Planning Unit (MAMPU) has issued guidelines and policies, such as the Open Data Implementation Manual, to promote data sharing across government agencies. However, these measures do not fully encompass all aspects of data sharing and lack the necessary enforceability to ensure comprehensive compliance.”

A similar process can be used to get answers[ to each of the sub-questions for this Barometer indicator.](https://handbook.globaldatabarometer.org/2021/indicators/G.GOVERNANCE.DATASHARING/)

The situation created is an interesting one:

* The prose generated by ChatGPT is, in many cases, clearer than the prose that comes from country researchers (in both the Open Data Barometer, and the Global Data Barometer, it proved prohibitively time consuming to edit all the justifications for consistency). 
* We have got clear answers to the questions that _appear_ to track, at some level, the likely situation in each country.

But:

* The answers are not based on research, and do not _actually _track the truth of the situation in each country. 
*  Because of the convincing justification offered, it is likely that LLM generated answers would pass many of the current review processes in which regional, or domain (but not country) experts quality assure responses.

 So, we’re in a situation where, at the very least,

* Some researchers may be incentivised to use LLMs to respond to their surveys (after all, they are generally paid a flat rate for completing the survey, and this could mean saving a _lot_ of time) and it may be hard to detect when this has happened; 
* Even researchers who don’t directly use LLMs are now operating in an environment where there may be more LLM generated text online, and they need to be more critical about source texts and references.

In all the hype around LLMs, some might argue that we should simply ‘lean in’ to completing expert surveys by machine: arguing that, over time, such systems will improve in their ability to generate ‘true’ answers (for example, newer systems have live access to the Internet to look up sources, not just generate text based on their existing corpora). I don’t subscribe to this view (not least because _until _such time as machines are reliable and truthful, [not just truthy](https://en.wikipedia.org/wiki/Truthiness), it risks further polluting the epistemic environment, and there are significant issues of bias in the information LLMs are trained on that need to be intentionally redressed). However, I do think there may be:

* **Positive strategies** for the careful application of LLMs to support human-led expert survey studies; and
* **Defensive strategies** that need to be adopted to maintain the robustness of expert survey evidence in light of the negative impacts of LLMs on the epistemic environment.  

## Positive strategies: research support

I’ve been exploring how well-crafted prompts could surface possible starting points for their research.

For example, some of the potential questions I’ve been scoping for Measuring Data Values need to look at how far a country has adapted data collection and use in order to respond to the needs of minority communities. Using the prompt:

> “I am going to ask you about the situation in Egypt. Are there minority populations in this country that face systemic disadvantages? Please answer Yes or No, followed by a short justification of two or three sentences.”

We can rapidly generate contextual information that researchers could be asked to (a) validate with their own knowledge and research; and (b) take into account in the research that follows:

> “Yes. Egypt is a majority-Muslim country, and the Coptic Christian minority population faces systemic disadvantages, including discrimination in employment and education, as well as restrictions on religious freedom. Additionally, the country's Bedouin population is often marginalized and excluded from access to basic services.”

In the past I looked at trying to bring in background information to support researchers to the Barometer survey tool from platforms like Wikipedia, or from structured datasets – but found coverage issues make that difficult (i.e. there are few sources that provide standardised coverage of the whole range of survey countries).

It would require testing to check that providing ‘background suggestions’ through LLMs is actually helpful to researchers, and is not subject to problematic biases. However, I suspect it’s worth exploring more.

## Positive strategies: refining questions

LLMs may also be useful for testing out expert survey questions, providing a rapid feedback loop to help in early question development.

There are some analogies between crafting a prompt for an LLM, and crafting questions and guidance for researchers. Terms need to be clearly defined, and guidance given on what constitutes a well justified answer.

By rapidly testing questions against LLM responses for a diverse range of countries, it may be possible to identify ways to improve questions prior to otherwise expensive pilot studies.

## Possible strategies: improving justifications and prose

The Barometer asks researchers to provide supporting evidence and justifications. In some cases, the justifications provided may not be relevant to the question. In other cases, the prose may include turns of phrase that do not work well in English.

An LLM can be asked to rephrase prose to a standard pattern, as in this example from a question on data management in Egypt:

> “Please rephrase the following text to remove value judgements and adopt a neutral tone. If it is longer than four sentences, please summarise. Provide references as footnotes where available. "What could be concluded here is that that data management and publication guidance does not exist in a clear framework in Egypt. The whole responsibility lies on the person conducting the management and at the same time scientific honesty to mention the data resource. Some places manage to declare those instructions but that is only an individual effort and not a governmental entity.”

Which results in the following prose:

> “It can be observed that Egypt lacks a clear framework for data management and publication guidance. The responsibility for managing and disclosing data sources solely rests with the individual conducting the research and their commitment to scientific honesty. Although some organizations may provide instructions for data management, these efforts are limited to individual initiatives rather than being mandated by a governmental entity.”

It may also be possible to integrate LLM chatbot features to support a more interactive research process, in which a survey tool might assess the quality of responses and ask researchers to provide more detail. For example, I promoted ChatGPT to evaluate a response and suggest possible information sources to check:

> “You are assessing the evidence that a researcher has provided. Does the extract below does not provide information about one or more specific data management policies, referenced by citation or name? If it does not, directly address the researcher and ask if they have checked relevant sources. Provide a list of suggested sources or research steps to explore. "What could be concluded here is that that data management and publication guidance does not exist in a clear framework in Egypt. The whole responsibility lies on the person conducting the management and at the same time scientific honesty to mention the data resource. Some places manage to declare those instructions but that is only an individual effort and not a governmental entity.”

Response:

> “Based on the provided extract, it does not specifically mention any data management policies by name or citation. It would be helpful to check relevant sources to gather more information and ensure the accuracy of the assessment. Here are some suggested steps to explore:
>
> 1.     Check official government websites and publications: Look for any data management policies or guidelines issued by relevant government entities in Egypt. The Ministry of Communications and Information Technology or the National Research Center could be potential sources to investigate.
> 2.     Research academic institutions: Explore the websites or publications of universities or research institutions in Egypt to see if they have specific data management policies or guidance.
> 3.     Consult international organizations: Organizations such as the World Bank or the United Nations may have conducted assessments or studies on data management practices in Egypt, which could provide valuable insights.
> 4. Engage with local experts: Reach out to professionals or researchers who are knowledgeable about data management practices in Egypt. They may be able to provide additional information or direct you to relevant sources.
>
> By conducting further research using these steps, you can gather more comprehensive and accurate information about the existence of data management policies in Egypt.”

However, any such approach would need significant testing to make sure (a) it does not distort the research process by giving different researchers different guidance (potentially correlated with particular factors such as a countries level of development, or the availability of online information about that country); (b) it is able to correctly assess when appropriate forms of evidence are, or are not, present – at least as reliably as a human reviewer may be able to.  

## Defensive strategies

Whether or not the above strategies are explored to integrate LLMs into an expert survey research process, it is likely that the review process will need to be strengthened to ensure that assessments and evidence presented are well sourced and supported. Possible approaches here may be to:

* Rely more on multiple experts per country and expert opinion (e.g. ask multiple experts for a subjective judgement of how effective data management frameworks are in the country, and take a (weighted) average of their judgements) as opposed to single researchers and source citations.
* Increase in-depth spot-checks on evidence to make sure claims are supported by evidence.
* Provide robust researcher training and guidance on where LLMs can and cannot be used as part of the research process.

## Exploring further

Ultimately, any engagement with LLMs as part of expert survey work should be based on much more in-depth testing and exploration, including work to:

* Assess the strengths and weaknesses of different LLMs;
* Understand the biases of particular models (including language biases), and assess whether these can be mitigated, or whether they present a fundamental limitation on LLM use;
* Further consider ethical and legal issues of using LLMs trained on information gathered without clear consent of the content creators;
* Understand the impact of LLM integration on the overall research workflow, including the motivation and engagement of researchers (including researchers from different cultures and backgrounds), and assess how their use impacts the overall quality of research.

Given the knowledge cut off of a number of LLMs is 2019, matching the first edition of the Global Data Barometer, there may be an interesting opportunity to do some of the above testing by comparing LLM survey responses with the Barometer researcher’s assessments. However, that’s a project beyond the scope of this short(ish) post.