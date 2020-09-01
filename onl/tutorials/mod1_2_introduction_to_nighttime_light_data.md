# Introduction to nighttime light data (10 min)

## Remotely sensed data of nighttime lights

The Defence Meteorological Satellite Program (DMSP) is based upon a 
series of Earth-orbiting satellites that were originally used to observe 
weather-related indicators at day and night, in the visual and in the infrared 
wavelength range. In 1973, Croft {cite}`croft1973burning` first reported that information collected in the 
Visible and Near-Infrared (VNIR) band is able to capture various sources of 
emissions from Earth, such as from city lights, auroras, gas flares, and fires; 
many of these sources can indicate aspects of human activity on Earth. 

### DMSP-OLS
The Operational Linescan System (OLS) is an oscillating scan radiometer 
with low-light visible and thermal infrared (TIR) imaging capabilities, 
which was first flown on DMSP satellites in 1976. In 1992, the 
National Oceanic and Atmospheric Administration/National Geophysical Data Center 
(NOAA/NGDC) established a digital archive of the collected scenes. 
With 14 orbits per day, each OLS is capable of generating global daytime and 
nighttime coverage of the Earth every 24 hours. Six satellites (i.e., F10, F12, F14,
 F15, F16, and F18) carrying the OLS have been launched since 1992.

Until now, the DMSP archive was processed and provided to the 
public on annual increments (data captured by each satellite was used to 
produce a time series of global cloud-free stable lights products with a 
spatial resolution of 30 arc sec, approximately 1Km at the equator). 
This data has been made available by the NOAA`s 
National Center for Environmental Information.

<div class="alert alert-success">
DMSP archive data has been made available by <a href="https://ngdc.noaa.gov/eog/dmsp/downloadV4composites.html" class="alert-link">NOAA`s 
National Center for Environmental Information</a>
</div>

**DMSP-OLS satellites by year**

|      | F10     | F12     | F14     | F15     | F16     | F18     |
|------|---------|---------|---------|---------|---------|---------|
| 1992 | F101992 |         |         |         |         |         |
| 1993 | F101993 |         |         |         |         |         |
| 1994 | F101994 | F121994 |         |         |         |         |
| 1995 |         | F121995 |         |         |         |         |
| 1996 |         | F121996 |         |         |         |         |
| 1997 |         | F121997 | F141997 |         |         |         |
| 1998 |         | F121998 | F141998 |         |         |         |
| 1999 |         | F121999 | F141999 |         |         |         |
| 2000 |         |         | F142000 | F152000 |         |         |
| 2001 |         |         | F142001 | F152001 |         |         |
| 2002 |         |         | F142002 | F152002 |         |         |
| 2003 |         |         | F142003 | F152003 |         |         |
| 2004 |         |         |         | F152004 | F162004 |         |
| 2005 |         |         |         | F152005 | F162005 |         |
| 2006 |         |         |         | F152006 | F162006 |         |
| 2007 |         |         |         | F152007 | F162007 |         |
| 2008 |         |         |         |         | F162008 |         |
| 2009 |         |         |         |         | F162009 |         |
| 2010 |         |         |         |         |         | F182010 |
| 2011 |         |         |         |         |         | F182011 |
| 2012 |         |         |         |         |         | F182012 |
| 2013 |         |         |         |         |         | F182013 |

## Limitations and challenges of DMSP-OLS

Inference using DMSP-OLS nighttime-light data may be challenging, 
particularly in low-density urban areas {cite}`zhang2013can`. 
DMSP-OLS tends to exaggerate the extent of urban areas {cite}`henderson2003validation,small2005spatial`, 
while overlooking small or developing settlements. 
The extent and intensity of lit areas cannot directly delimit urban regions due to the 
“blooming” effect [NEED CITATION] (Imhoff et al., 1997) and “saturation” of pixels [NEED CITATION](Hsu et al., 2015).

<div class="alert alert-info">
<b>Blooming</b> refers to the identification of lit areas as consistently larger than the settlements with which they are associated.
</div> 

{cite}`small2005spatial`

Blooming results in from three primary phenomena: 
- (1) the relatively coarse spatial resolution of the OLS sensor and the detection of 
diffuse and scattered light over areas containing no light source , 
- (2) large overlap in the footprints of adjacent OLS pixels, and 
- (3) the accumulation of geolocation errors in the compositing process.
{cite}`elvidge2004area`

<div class="alert alert-info">
<b>Saturation</b> occurs when pixels in bright areas, such as in city centers, 
reach the highest possible digital number (DN) value (i.e., 63) 
and no further details can be recognized [NEED CITATION] (Hsu et al., 2015).
</div>

**Lack of on-board calibration.** Due to the absence of on-board calibration, 
the DMSP/OLS stable NTL annual composites product derived from multiple sensors 
(F12–F16) and different years (1992–2013) are not comparable directly. {cite}`doll2008ciesin`


## Addressing the lack of on-board calibration

Generally speaking, DMSP-OLS “raw” data cannot be used “as-is” for temporal analysis due, 
in part, to its interannual instability and deviations between sensors in the same year. 
In order to compare this data across time, the data collected by the sensors on board these 
satellites must be inter-calibrated to account for the lack of on-board calibration, varied 
atmospheric conditions, satellite shift, and sensor degradation.

One of the most used frameworks for inter-calibration of DMSP-OLS annual composites 
was proposed by Elvidge  et al. (2009) {cite}`elvidge2009fifteen`. This procedure relies on a manual selection of 
Pseudo-Invariant Features (PIF), a reference satellite and year for calibration and a 
quadratic regression model to estimate the DN value of pixels in different years 
(in comparison to a reference image). Elvidge et al. chose the annual composite of 
F12 satellite from 1999 (i.e. F121999) as the reference for calibration (in other words, 
all other satellite years were adjusted to match the F121999 data range). Sicily, Italy, 
was selected as the region for calibration (or as the PIF). PIFs are essentially areas where 
nighttime light emission is expected to be relatively stable over time and where we would not 
expect to see much variation between satellites and years. Following studies have proposed 
different types of regression models, PIFs or reference satellites to perform the 
intercalibration procedure. In this course we will adopt the calibration coefficients 
proposed by Elvidge et al. for the intercalibration procedure {numref}`elvidge2009` (don`t worry. we will describe 
the inter-calibration procedure in the next modules).


```{figure} img/mod1-elvidge2009.png
---
name: elvidge2009
---
DMSP-OLS intercalibration {cite}`elvidge2009fifteen`
```

## The new and improved nighttime light sensor: VIIRS-DNB

The Visible Infrared Imaging Radiometer Suite (VIIRS) is an instrument mounted on the 
Suomi-NPP satellite. It was launched in late 2011 and has been collecting data since early 2012. 
Within the VIIRS instrument, the Day/Night Band (DNB) Detector collects global low-light 
imaging data, with significant improvements over DMSP-OLS. One of the prominent features of 
DNB data is the detection of electric lighting present on the Earth’s surface.

<div class="alert alert-success">
For detailed information on the VIIRS instrument, see the <a href="https://ncc.nesdis.noaa.gov/documents/documentation/viirs-users-guide-tech-report-142a-v1.3.pdf" class="alert-link">VIIRS Users Guide Technical Report</a>
</div>

VIIRS, while assessed to be more efficient at measuring economic activities via 
nighttime light analysis, is not without limitations. Because of the highly sensitive nature 
of the VIIRS sensor, it also detects phenomena that are not related to surface lighting, 
for example, traces of reflected sunlight, stray light, lightning, aurora, biomass burning, etc. {cite}`elvidge2009fifteen`
This is what makes the filtering process for VIIRS data so important. The procedure for 
generating VIIRS night-time lights into a usable product (e.g. weekly, monthly or annual composites) 
involves a multi-step process to filter extraneous features (e.g. sunlight, moonlit, stray light, 
outlier removal, background seeds, surface lighting, and gas flares), followed by an averaging of 
the radiance values. These procedures were described by Elvidge et al. {cite}`christopher2017viirs`, and continue to be improved 
upon.

**In this course:** we will implement similar methods to produce “clean” composites 
that filter this noise.

## DMSP-OLS vs. VIIRS
As previously stated, VIIRS is considered a superior data product when analyzing nighttime lights, 
largely due to the increased spatial resolution. Shi et al. (2014) {cite}`shi2014evaluating` 
outline three improvements VIIRS data has over DMSP-OLS: 
- A higher spatial resolution (15 arc-second (~500 m) versus 30 arc-second (~1,000 m with DMSP-OLS); 
- Over-saturation is less of a problem with VIIRS than it is with DMSP-OLS (due to a wider radiometric detection range); and
- VIIRS data employ onboard calibration which increases the data quality.

The following table {numref}`elvidge2013` provides a detailed side-by-side comparison 
of the two products:
```{figure} img/mod1-elvidge2013.png
---
name: elvidge2013
---
DMSP-OLS vs SNPP-VIIRS {cite}`elvidge2013viirs`
```
## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```