# High Resolution Electricity Access (HREA) Indicators

## New methods to estimate electricity access using nightly VIIRS satellite imagery

Brian Min and Zachary O'Keeffe at the University of Michigan have created 
a statistical model that generates likelihood estimates of 
electricity access for all areas with human settlements for a given country.

<a href="https://github.com/zachokeeffe/nightlight_electrification">The source repository is available here.</a>

This repo contains scripts (scripts are in R) and more details about the data and methods used.

### Introduction

We introduce a new method to generate likelihood estimates of electricity access for all areas with human settlements within a country by identifying statistical anomalies in brightness values that are plausibly associated with electricity use, and unlikely to be due to exogenous factors.

On every night, the VIIRS DNB sensor collects data on the observed brightness over all locations within a country, including over electrified and unelectrified areas, and populated and unpopulated areas. Our objective is to classify populated areas as electrified or not using all the brightness data over a country. But the challenge is that light output can be due to multiple sources unrelated to electricity use. Notably, the VIIRS sensor is so sensitive that it picks up light from overglow, atmospheric interactions, moonlight, and variations in surface reflectivity across types of land cover. We refer collectively to these exogenous sources as background noise, which must be accounted for to classify whether an area is brighter than expected.

We use data on light output detected over areas with no settlements or buildings to train a statistical model of background noise. The model can be used to generate an expected brightness value on every given night for every given location. We then compare the observed brightness on each night against the expected baseline brightness value. Areas with human settlements with brighter light output than expected are assumed to have access to electricity on that night. We classify all settlements on all nights and then average the estimates and generate an "Artificial Light Score" for each calendar year for all settlement areas. Areas that are much brighter than would be expected on most nights have the highest probability of being electrified. Areas that are as dim as areas with no settlements have the lowest probability of being electrified. And areas that are a little brighter on some nights have middling scores.

The advantage of this process is that it uses all available nightly data from the VIIRS data stream while taking into account sources of known noise and variability. The process also allows for the identification of areas where the likelihood of electricity access and use is uncertain (the areas with middling scores). This is significant given that traditional binary measures of access do not account for variations in levels of use or reliability of power supply, even across areas that are all nominally electrified. These data may therefore be helpful in identifying baseline variations in access and reliability within countries, consistent with the objectives of the Multi-tier Framework for measuring energy access (ESMAP 2015).