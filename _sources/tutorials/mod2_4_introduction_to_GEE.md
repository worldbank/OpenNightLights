# Introduction to Google Earth Engine (GEE) (5 min)

## Google Earth Engine (GEE) Overview

<div class="alert alert-success">
<a href="https://earthengine.google.com/" class="alert-link">Google Earth Engine (GEE)</a> is a cloud-based platform for planetary-scale geospatial analysis which allows to process a variety of geographical data at scale and handle large geographical datasets. 
</div>

Since geographical data are often large and complicated to store, GEE provides a quickly accessible collection of ready-to-use data products. In addition, it is open and free to the public (for non-commercial use).

GEE consists of a multi-petabyte “ready-to-use” data catalog alongside a high-performance, intrinsically parallel computation service. It can be accessed and controlled through an Internet-accessible application programming interface (API) and an associated web-based interactive development environment (IDE) that enables rapid prototyping and visualization of results {cite}`gorelick2017google`.

Because all the datasets are available on the GEE platform, there is no need to manage the data, download them, change the file format, or update the geographic projection. It uses the power of thousands of computers located in Google data centers to carry out its heavy processing. This distributed network allows the user to finish a task in a few minutes for small areas and few days for a world-scale study. 

GEE provides access to numerous remotely sensed datasets and derived products, including DMSP-OLS and VIIRS DNB. Some of the data is already provided  in the platform processed and “ready-to-use”. 

<div class="alert alert-success">
<a href="https://groups.google.com/u/1/g/google-earth-engine-developers?pli=1" class="alert-link">The GEE developer forum</a> is a very helpful resource for beginners. On this forum it is possible to directly ask a question to the GEE community including GEE programmers and founders. 
</div>

## GEE Access
Accessing GEE is easy. Aspiring users will first need to <a href="https://signup.earthengine.google.com/" class="alert-link">sign up to the platform</a> with their Google account. It is the same account, people use to access Youtube, Google drive, Gmail and any Google service. Google usually gives access to new users within 24 hours. Then, all a user needs to access GEE from anywhere in the world is an internet connection.

Data in GEE can be analyzed in two ways:  
- 1) through the Javascript API via the GEE code editor, or 
- 2) a Python API, geemap, that can be accessed through any Python environment, such as Jupyter notebooks. More on that in {doc}`mod2_5_GEE_PythonAPI_and_geemap`

### GEE Code editor
<a href="https://code.earthengine.google.com/">code.earthengine.google.com</a> is the code editor that uses JavaScript to access, transform, analyze, visualize and manage satellite data in GEE.

<div class="alert alert-success">
The GEE platform provides <a href="https://developers.google.com/earth-engine/" class="alert-link">comprehensive documentation</a> and tutorials with videos as well as an  Application Programming Interface (API) dictionary to help users to learn how to write and use every JavaScript function in GEE.
</div>

### Get to know the data
It will really help you to understand some of the exercises in this tutorial if you spend a little time getting familiar with the data in GEE.

For example, take a look at the <a href="https://developers.google.com/earth-engine/datasets/catalog/NOAA_DMSP-OLS_NIGHTTIME_LIGHTS">DMSP-OLS dataset description</a> in GEE. It provides summary information on how the data are collected and organized and what they represent as well as links to more detailed technical information on the source. You'll also notice an "Earth Engine Snippet" (such as: `ee.ImageCollection("NOAA/DMSP-OLS/NIGHTTIME_LIGHTS")` -- we will re-visit this as it is the key for pulling particular datasets in GEE.

You can also review the page on <a href="https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG">VIIRS-DNB stray-light corrected monthly composites</a> in GEE.

You may notice that many datasets have multiple vintages and versions. The description usually give insight into what this means (otherwise you may have to go to the source information), but it is important to understand that there can be differences in the data from particular satellite systems.

## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```


```python

```
