# Introduction to remote sensing (20 min)

## What is remote sensing?

<div class="alert alert-info">
<b>Remote sensing</b> is the science of identifying, observing, collecting and measuring objects without coming into direct contact with them.
</div>
 
This can be accomplished through many devices that carry sensors and capture the characteristics of Earth remotely.

```{figure} img/mod1-remote_sensing.png
---
name: remote-sensing
---
Remote sensing<br>
Source: {cite}`NASA_goddard_2017`
```
Sensors on board satellites also record the electromagnetic energy that is reflected or emitted from objects on Earth.

### Passive and Active Sensors
Sensors on board satellites can be classified into two main categories: Passive and Active.

<div class="alert alert-info">
<b>Passive sensors</b> record the natural energy that is (naturally) reflected or emitted from the Earth's surface (e.g. sunlight, moonlight, city lights). 
</div>

<div class="alert alert-info">
<b>Active sensors</b> provide their own energy source for illumination (e.g. RADAR, LIDAR). 
</div>

#### Passive remote sensing
The energy of the sun is composed of many kinds of radiation, some of which spans the visible part of the electromagnetic spectrum. Many instruments collect Red, Green, and Blue bands of the spectrum (R,G,B) to create natural color images.

Meaningful information is also contained in parts of the spectrum outside the range of human vision, including infrared (IR) and ulta-violet (UV).

```{figure} img/mod1-light_spectrum.png
---
name: light-spectrum
---
Electromagnetic spectrum<br>
Source: {cite}`Hudedmani2017ASO`
```

The energy of the sun is absorbed or scattered by the atmosphere before it reaches earth.

In Remote Sensing analysis we aim to learn about objects on Earth through studying the radiation reflected and/or emitted by them. 

```{figure} img/mod1-radiation.png
---
name: radiation
---
Reflected and emitted radiation<br>
Source: {cite}`phdthesis`
```

## Spatial, spectral and temporal resolutions in remote sensing

Remote sensing instruments are characterized by different resolutions which will impact the decision as to which data to use and for which application (this is often referred to as “Fit-for-Purpose” technologies).

### Spatial resolution

<div class="alert alert-info">
<b>Spatial resolution</b> signifies the ground surface area that forms one pixel in the image. Sub-pixel objects can sometimes be resolved. 
</div>

For example, dirt roads in Figures 1.4 are smaller than the 30 m Landsat pixels, but are still detected.

```{figure} img/mod1-landsat7.png
---
name: landsat-7
---
Landsat-7 (30 m)
```

```{figure} img/mod1-sentinel2.png
---
name: sentinel2
---
Sentinel-2 (10 m)
```

```{figure} img/mod1-worldview.png
---
name: worldview
---
Worldview (50 cm)
```

**In this course:** we will be working primarily with VIIRS-DNB and DMSP-OLS VNIR band data. Their spatial resolutions are approximately 750m and 2.7km , respectively.

### Spectral resolution
<div class="alert alert-info">
<b>Spectral resolution</b> signifies the number and width of spectral bands of the sensor. The higher the spectral resolution, the narrower the wavelength range for a given channel or band. 
</div>

Typically, multispectral imagery refers to 3 to 10 bands, while hyperspectral imagery consists of hundreds or thousands of (narrower) bands (i.e. higher spectral resolution) (see Figure 1.7). Panchromatic is a single broad band that collects a wide range of wavelengths. 

```{figure} img/mod1-hyperspectral.png
---
name: multi_and_hyperspectral
---
Multispectral and hyperspectral imagery<br>
Source: {cite}`GISGeography`
```

**In this course:** we will be working with VIIRS-DNB and DMSP-OLS data, which have single panchromatic channels covering the wavelengths ranging from 500 to 900 nanometers.

### Temporal resolution
<div class="alert alert-info">
<b>Temporal resolution</b> refers to the repeat cycle, or frequency, with which a sensor revisits the same part of the Earth’s surface. You might hear this referred to as a satellite’s “revisit time.” 
</div>
 
Generally speaking, the larger the swath width of a polar orbiting satellite, which you can think of as the width of the sensor’s field of view “cross-track” (or “left to right”) during an orbital pass , the higher the temporal resolution. This is because more of the earth is imaged in a single pass of the satellite.

### Trade-offs in remote sensing resolution:
There is an inherent tradeoff between spatial, spectral and temporal resolutions. Typically, the higher the spatial resolution, the lower the spectral and the temporal resolution and the higher the temporal resolution, the lower the spatial and spectral resolutions (Figure 1.8).

```{figure} img/mod1-res_tradeoffs.png
---
name: res_trade-offs
---
Trade-offs with spatial, spectral, and temporal resolution. The figure illustrates some of the tradeoffs in remotely sensed data.  For example, sensors that collect images in a high spatial resolution, will typically have lower spectral (less bands) and low temporal (less frequent re-visit) resolutions. On the other hand, the spatial and spectral resolution of sensors with a high temporal resolution (frequent revisit) will typically be lower than sensors that collect data in a low temporal resolution (less frequent revisit).<br>
Source: {cite}`warner2009remote`
```

**In this course:** we will be using VIIRS-DNB and DMSP-OLS data. Both of these sensors image the same earth location at least once during the day and once during the night. We’re only interested in the nighttime pass, so our data can be considered to have a daily temporal resolution. However, as we will learn, it’s helpful to temporally aggregate data to account for noise or obstructions, such as cloud-cover, so our final analysis may end up using composite data that has time periods of up to a month or year.

<div class="alert alert-success">
For detailed information on the VIIRS instrument, see the <a href="https://ncc.nesdis.noaa.gov/documents/documentation/viirs-users-guide-tech-report-142a-v1.3.pdf" class="alert-link">VIIRS Users Guide Technical Report</a>. For detailed information on DMSP-OLS, see [need citation].
</div>

## Applications of remotely-sensed derived data in socio-economic research

Remotely sensed observations are useful for a wide-range of economic research applications. Donaldson and Storeygard {cite}`donaldson2016view` outline some advantages of using remotely sensed data for economic studies:

**1. Improved accessibility to information difficult to obtain by other means:**

Remote sensing technologies can collect panel data at low marginal cost, repeatedly, and at large scale, providing proxies for a wide range of characteristics that are hard (or impossible) to measure by other means.

**2. High(er) spatial resolution:**

Remotely sensed data are typically available at a higher spatial resolution than other traditional data sources, for example, census data (which is available at the geographical unit of the census tract, the block group etc.).  Publicly available satellite imagery  used by economists provide measurements of every location on Earth and are not constrained to a specific scale in which the data was collected at or aggregated to. 

**3. Wide geographic coverage and high temporal resolution:**

Data collected by satellites provide continuous and consistent observations of phenomena on Earth, regardless of the conditions on the ground (e.g. political strife or natural disasters), across borders, including inaccessible locations and with a uniform spatial sampling. Satellites have substantial temporal coverage, capturing every location on Earth on a daily or weekly basis. Some archives date back to  the 1970s.

**Nighttime lights are especially useful for a variety of socio-economic research and applications.** There is a strong correlation between nighttime lights and Gross State Product (GSP) or Gross Domestic Product (GDP) measures, at the national, state and regional levels {cite}`henderson2012measuring,ghosh2010shedding,chen2011using` or even at a more granular resolution. Thus, nighttime light observations can be used as a proxy for economic activity, especially over periods or regions where these data are not available or where the statistical systems are of low quality or when no recent population or economic censuses are available. Similarly, changes in nighttime light intensity can be used by economists as an additional measure of income growth when no other measures of income growth are available.

```{figure} img/mod1-elvidge-gdp-ntl.png
---
name: gdpvsntl
---
Area of lighting versus GDP for 200 countries of the world. (from Elvidge et al., 2001) {cite}`elvidge2001night`
```

**Comparing nighttime lights and a series of socio-economic indicators:** 
Proville et al. (2017) {cite}`proville2017night` examined trends observed by DMSP-OLS in the period 1992-2013 and their correlation with a series of socio-economic indicators. {numref}`proville` They found the strongest correlations between nighttime lights, electricity consumption, CO2 emissions, and GDP, followed by population, CH4 emissions, N2O emissions, poverty and F-gas emissions.  

```{figure} img/mod1-proville.png
---
name: proville
---
Various socio-economic indicators vs DMSP-OLS nighttime lights measures{cite}`proville2017night`
```

**Natural characteristics of Earth and nighttime lights:**
Henderson et al. (2018) {cite}`henderson2018global` explored whether - and which - of the natural characteristics of Earth can explain the spatial distribution of economic activity worldwide, at least according to nighttime lights. The authors found that 24 physical geographic attributes can explain up to 47% of worldwide variation and up to 35% of the variation of lights within countries.

Among countries that developed early, agricultural variables incrementally explain over 6 times as much variation in lights as do trade variables. On the other hand, among late developing countries, the same ratio is only about 1.5, despite the fact that these countries are far more dependent on agriculture.

## Summary
Remote sensing instruments collect electromagnetic energy to map a variety of phenomena on the earth’s surface. These instruments typically trade between three categories of performance: spatial, spectral, and temporal. Remotely sensed imagery can reach all parts of the earth at a consistent resolution, and some archives span decades into the past. For this work we will focus on nighttime lights from the VIIRS-DNB and DMSP-OLS sensors. There is a long and significant body of research showing correlation between nighttime lights and a variety of useful socio-economic variables.

## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```