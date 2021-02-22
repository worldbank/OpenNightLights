# Framing the analysis

The most important work in any real-world problem-solving is framing your analysis in order to provide the most meaningful insights.

The scientific process and communicating about data for decision-makers are big but important topics for another tutorial. But some high level guidance for data anlysis is useful here:
- What is the key inquiry?
- What are possible testable hypotheses?
- What data?
- What methods?
- What conclusions are possible?

## What is the key inquiry?

This is one of the most important steps of any analysis and should be done collaboratively with stakehoders. We're making some assumptions about land use and economic activity, so this is where the researcher will do extensive literature review to make sure this is a valid approach and one that, if conducted, actually helps the stakeholders gain insight or make decisions. 

For this exercise, we'll assume this diligence was done and we are framing our analysis around: **detecting changes in land cover that indicate changes in economic activity over the course of 5 years in the country of Nepal, from 2015 through 2019.**

## What are possible testable hypotheses?

In an academic or clinical setting or with high stakes for decision-making, analysis needs high levels of rigor to answer if there was an observed effect. We will frame this as exploratory analysis, so we can be a bit more relaxed, but it is still a good idea to set a threshold for what we are looking for **before** we look at the data. 

We will keep things simple. We are trying to detect change and we are making an assumption that land cover can proxy economic activity in a way that is useful for our stakeholders. Our testable hypothesis will therefore be: **whether or not there are significant changes in land cover in Nepal in 2019 compared to 2014.** The null hypothesis is that there is no change in either direction (growth or decline), a two-tailed hypothesis. Will our data be able to reject that?

## Data

There are key considerations when identifying data that will help us answer our inquiry.

- We are trying to define land cover, so spatial (and spectral) resolution are important at a high enough precision where we can distinguish changes to particular cities and towns, i.e. spatial resolution at least at the neighborhood level.

- We are looking at changes in time, so clearly temporal resolution is important as well.

- We are concerned with the entire country of Nepal during 2015 to 2019, so uninterrupted geospatial and historical coverage of Nepal during those years is important.

- For remote sensing, as with many sources of big data, we will want to understand the quality of the data and any preprocessing that has been done, or which we would need to do.

- Are the data accessible, affordable (or free) and available long-term, so that an extension or reproduction of our research at a later date is possible?

- Given the types of data (e.g. nighttime lights), what specific data products are available?

Given these considerations, for identifying land use and land cover:
- VIIRS-DNB monthly composites for nighttime lights;
- Supplemented with Sentinel-2 daytime visible band images (monthly composites)

...will provide the information we need. And as a way to define built-up areas (i.e. our training labels):

- Global Human Settlement Layer (GHSL), which we have available most recently in 2015.

## Methods

As with defining our inquiry and choosing data, choosing our approach should include research and diligence about appropriate methods.

We are fortunate to have found a dataset, the GHSL data, that tells us what we want to know: settlement locations, i.e. built-up area. This is exactly what we are trying to measure, so we can use this dataset to define what constitues "built-up" or "not built-up" in terms of land cover.

There is a problem; however, these data are available only as recently as 2015. We do not have GHSL data for 2016-2019 and measuring the change in built-up land use over that time is the whole point of our research.

We know our remote sensing data, the VIIRS-DNB and Sentinel-2 data collections, do cover change during this period with adequate temporal precision, but these data do not explicitly define "built-up" areas. We'll have to infer what is "built-up" from 2015 to 2019 in order to measure change. Therefore, we will use image classification via a supervised learning method. 

Since we are using data from three separate sources (VIIRS, Sentinel-2, GHSL) we will need to integrate them into a dataset that is aligned spatially and temporally, a process sometimes described as data fusion.

We will train a clssifier using VIIRS-DNB and Sentinel-2 data for 2015, the year we have GHSL validation data, to classify a pixel as being "built-up" or "not built up." There is extensive research available on supervised learning classifier algorithms avialable, but one of the most commonly used and generally effective across a large range of domains and problems is an ensemble decision tree-based model called Random Forest (RF). RF also happens to be available as in Google Earth Engine (GEE) so we do not have to implement this algorithm from scratch.

We will use this trained model on VIIRS-DNB and Sentinel-2 data for the years we do not have GHSL data (2016-2019) to classify pixels as "built-up" or not.

Finally, we can analyze the change with some visualizations and importantly, conduct a statistical test of variance that compares Nepal in 2019 with Nepal in 2015 and will either reject our null hypothesis (no change) or fail to reject it.

## Conclusions

We should be able to communicate the findings of our statistical analysis (i.e. whether we saw change in economic activity or not). 

Whatever the outcome, we should also be able to justify our decisions, assumptions and approach so that it stands up to scrutiny and follow-up analysis, which is a part of any real-world decision-making process. 

Finally, in addition to our primary analysis, we should be prepared to describe any other insights or that might be useful. For example, in addition to the overal change in activity from 2015-2019, are there any particular trends or patterns worth noting?