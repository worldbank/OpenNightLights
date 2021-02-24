# Framing the analysis

The most important work in any real-world problem-solving is framing your analysis in order to provide the most meaningful insights.

The scientific process and communicating about data for decision-makers are big but important topics for another tutorial, but some high level guidance for data anlysis is useful here:
- What is the key inquiry?
- What are possible testable hypotheses?
- What data is needed?
- What methods are useful?
- What conclusions are possible?

## What is the key inquiry?

This is one of the most important steps of any analysis and should be done collaboratively with stakehoders. We are making some assumptions about land use and economic activity, so this is where the researcher will do extensive literature review to make sure this is a valid approach and one that, if conducted, actually helps the stakeholders gain insight or make decisions. 

If this is a particularly relevent research inquiry (beyond learning the skills), there is plenty of literature on the use of remote sensing to monitor changes in land use {cite}`dewan2009land`, including nighttime lights {cite}`jiang2020detecting` and we draw draw attention to nighttime lights applications to economic analysis of course, {doc}`mod1_2_introduction_to_nighttime_light_data`. There are also many instances on the growing application of machine learning prediction for land use and ultimately economic development, simliar to our scope here {cite}`liping2018monitoring`.

For this exercise, we'll assume this diligence was done and we are framing our analysis around: **detecting changes in land cover that indicate changes in economic activity over the course of 4 years in the country of Nepal, from 2016 through 2019.**

We do not yet have a full year of data for 2020 as of the writing of this tutorial, but there is a clear opportunity for you to expand on this at home.

## What are possible testable hypotheses?

In many settings typically analysis needs high levels of rigor to answer if there was an observed effect. We will frame this as exploratory analysis for learning purposes, so we can be more relaxed, but it is still a good idea to clarify what we are looking for and what our threshold will be for an effect **before** we look at the data. We are trying to detect change and we are making an assumption that land cover can proxy economic activity in a way that is useful for our stakeholders. 

Our testable hypothesis will therefore be: **whether or not there are significant changes in land cover in Nepal in 2019 compared to 2016.** 

The null hypothesis is that there is no change in either direction (growth or decline), a two-tailed hypothesis (with a p value below 0.05). Will a comparison of the distribution in built-up land cover in 2016 versus 2019 be able to reject that?

## Data

There are key considerations when identifying data that will help us answer our inquiry.

- Spatial (and spectral) resolution are important at a high enough precision where we can distinguish changes to particular cities and towns, i.e. spatial resolution at least at the neighborhood level.

- Clearly temporal resolution is important as well.

- Uninterrupted geospatial and historical coverage of our Region of Interest in Nepal during these years is important.

- For remote sensing, as with many sources of big data, we will want to understand the quality of the data and any preprocessing that has been done, or which we would need to do.

- How accessible, affordable and available long-term (i.e. sustainable) are the data sources? And via what specific data products?

Given these considerations, for identifying land use and land cover we decide to use:
- VIIRS-DNB monthly composites for nighttime lights;
- Supplemented with Sentinel-2 daytime visible band images (monthly composites)

...will provide the information we need. And as a way to define built-up areas (i.e. our training labels):
- Global Human Settlement Layer (GHSL), which we have available most recently in 2015.

## Methods

As with choosing data, choosing our approach should include diligence about appropriate methods.

We are fortunate to have found a dataset, the GHSL data, that tells us what we want to know: settlement locations, i.e. built-up area. This is exactly what we are trying to measure, so we can use this dataset to define what constitues "built-up" or "not built-up" in terms of land cover.

There is a problem; however, these data are available only as recently as 2015. We do not have GHSL data for 2016-2019 and measuring the change in built-up land use over that time is the whole point of our research.

We know our remote sensing data, the VIIRS-DNB and Sentinel-2 data collections, do cover change during this period with adequate temporal precision, but these data do not explicitly define "built-up" areas. 

We'll have to infer what is "built-up" from 2016 to 2019 in order to measure change. Therefore, we will use classification via a supervised learning method. {doc}`mod6_2_supervised_learning_img_classification`

Since we are using data from three separate sources (VIIRS, Sentinel-2, GHSL) we will need to integrate them into a dataset that is aligned spatially and temporally, a process sometimes described as data fusion. {doc}`mod6_5_data_fusion`

We will train a clssifier using VIIRS-DNB and Sentinel-2 data for 2015, the year we have GHSL validation data, to classify a pixel as being "built-up" or "not built up." There is extensive research available on supervised learning classifier algorithms avialable, but one of the most commonly used and generally effective across a large range of domains and problems is an ensemble decision tree-based model called Random Forest (RF). RF also happens to be available as in Google Earth Engine (GEE) so we do not have to implement this algorithm from scratch. {doc}`mod6_6_RF_classifier`

We will use this trained model on VIIRS-DNB and Sentinel-2 data for the years we do not have GHSL data (2016-2019) to classify pixels as "built-up" or not.

Finally, we can analyze the change with some visualizations and importantly, conduct a statistical test of variance that compares our Region Of Interest (ROI) in Nepal in 2019 with the ROI in 2016 and will either reject our null hypothesis (no change) or fail to reject it. {doc}`mod6_7_final_analysis`

## Conclusions

We should be able to communicate the findings of our statistical analysis (i.e. whether we saw change in economic activity or not). 

Whatever the outcome, we should also be able to justify our decisions, assumptions and approach so that it stands up to scrutiny and follow-up analysis, which is a part of any real-world decision-making process. 

Finally, in addition to our primary analysis, we should be prepared to describe any other insights or that might be useful. For example, in addition to the overal change in activity from 2016-2019, are there any particular trends or patterns worth noting? Further research or data needed?

## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```