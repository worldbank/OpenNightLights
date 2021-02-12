# World Bank - Light Every Night

## Overview
World Bank Light Every Night is a comprehensive data repository of nighttime light satellite imagery collected from two sensors over the last three decades: the Defense Meteorological Satellite Program (DMSP) Operational Linescan System (OLS) with data from 1992-2017, and the Visible Infrared Imaging Radiometer Suite (VIIRS) Day-Night Band (DNB) with data spanning 2012-2020. 

The DMSP-OLS and VIIRS-DNB sensors capture various sources of low-light emissions from Earth. These include sources that indicate aspects of human activity, like city lights, gas flares, fishing boats, and agricultural fires, while also capturing other nighttime lights phenomena such as auroras.

The World Bank worked in collaboration with the National Oceanic and Atmospheric Administration (NOAA) and the University of Michigan to publish this repository, designed from the ground up to be analysis-ready. The underlying data are sourced from the NOAA National Centers for Environmental Information (NCEI) archive. Additional processing by the University of Michigan enables access in Cloud Optimized GeoTIFF format (COG) and search using the Spatial Temporal Asset Catalog (STAC) standard. These standards are part of the growing Analysis Ready Data ecosystem that is improving access to geospatial data sets, enabling broader audiences to readily discover, process and analyze geospatial data.

Learn more about remote sensing, nighttime light images and using these data for analysis at <a href="https://worldbank.github.io/OpenNightLights/welcome.html">World Bank's Open Nighttime Lights tutorial.</a>

## Accessing Light Every Night data on AWS
You can access these data via the link, `s3://globalnightlight` and using the web interface via the AWS console. Or via the AWS Command Line Interface, for example to list all files in the VIIRS 201505 sub-directory (using the `--no-sign-request` flag since this bucket is public:
```
$ aws s3 ls s3://globalnightlight/201505 --no-sign-request
```

## Light Every Night file structure
The data for both DMSP-OLS and VIIRS-DNB are in the root AWS S3 bucket, `s3://globalnightlight/`. DMSP-OLS data are organized into directories by satellite name and year. VIIRS-DNB data are organized by month until 2017 and by satellite name and month starting in 2018 when data from two satellites (NPP and NOAA-20/J01)  became available.

### DMSP-OLS
DMSP-OLS data are organized by satellite name and the year in which the data were captured. The DMSP satellites have the naming convention F[nn], where nn ranges from 10-18 for this collection. A table is provided below of DMSP satellites and the corresponding years for which nighttime OLS data are available in the Light Every Night AWS repository. While this is the bulk of the nighttime OLS data, other satellite-years and data from 2018-present are available and can be accessed by contacting the <a href="https://www.ngdc.noaa.gov/eog/dmsp.html">DMSP archive at NOAA/NCEI</a>. Matching the satellite name with a year available in the table gives the subdirectory in the AWS bucket, for example `s3://globalnightlight/F121995/` contains all data collected by DMSP satellite F12 in the year 1995.

**Table 1. DMSP satellites and their corresponding years of OLS data that are available in the World Bank Light Every Night repository.**

| F10 | F12 | F14 | F15 | F16 | F18 |
| --- | --- | --- | --- | --- | --- |
| 1992 |  |  |  |  |  |
| 1993 |  |  |  |  |  |
| 1994 | 1994 |  |  |  |  |
| | 1995 |  |  |  |  |
| | 1996 |  |  |  |  |
| | 1997 | 1997 |  |  |  |
| | 1998 | 1998 |  |  |  |
| | 1999 | 1999 |  |  |  |
| |  | 2000 | 2000 |  |  |
| |  | 2001 | 2001 |  |  |
| |  | 2002 | 2002 |  |  |
| |  | 2003 | 2003 |  |  |
| |  |  | 2004 | 2004 |  |
| |  |  | 2005 | 2005 |  |
| |  |  | 2006 | 2006 |  |
| |  |  | 2007 | 2007 |  |
| |  |  |  | 2008 |  |
| |  |  |  | 2009 |  |
| |  |  |  | 2010 | 2010 |
| |  |  |  |  | 2011 |
| |  |  | 2012 |  | 2012 |
| |  |  | 2013 |  | 2013 |
| |  |  | 2014 |  | 2014 |
| |  |  | 2015 |  |  |
| |  |  | 2016 | 2016 |  |
| |  |  | 2017 | 2017 |  |

Within a given sub-directory, data are provided by satellite orbit for every day (night) of the given year. For each OLS orbital segment, there are 5 image layers and a JSON metadata file. For a given orbital segment, these 6 files all have the same file prefix, which contains some metadata about the satellite and start time of the data in UTC. These are described below using an example:

```
F12199501010014.night.OIS
F12 -> satellite name
   1995 -> year at start of orbital segment
       01 -> month at start of orbital segment
         01 -> day of month at start of orbital segment
           00 -> hour of day at start of orbital segment
             14 -> minute of hour at start of orbital segment
               .night -> orbit is cropped to only nighttime data
                     .OIS -> acronym for OLS Interleaved Smooth
```
For each orbital segment, there are 5 image layers and the JSON metadata file. They have the same file prefix as described above, and are distinguished by their file extensions:
- `.vis.co.tif`: a COG with a single band containing the visible nighttime imagery (this is the key data file)
    - Data range: [0, 63]
    - “No-data” value: 255
    - Data type: byte
    - Units: Digital Number (DN) or unitless
- `.vis.co.json`: a JSON file following the STAC schema with metadata for orbital segment, including a timestamp and a geospatial bounding box
- `.flag.co.tif`: a COG with a single band containing bitflags that can be queried for data quality
    - Data range: [0,2<sup>15</sup>-1]
    - “No-data” value: 2<sup>15</sup>
    - Bit-fields: see Table 2
    - Data type: 16-bit integer
    - Units: Unitless
- `.tir.co.tif`: a COG with a single band containing the OLS Thermal Infrared (TIR) data
    - Data range: [0, 255]
    - “No-data” value: 255 (note this is not unique, use `vis.co.tif` or another companion file to confirm areas of no data)
    - Data type: byte
    - Units: Scaled byte data. These values can be converted to temperature in Kelvin using [slope, offset] of [0.4706,190.0]
- `.samples.co.tif`: a COG with a single band containing sample position for the OLS pixel along the swath.
    - Data range: [1,1465]
    - No-data value: 0
    - Data type: 16-bit integer
    - Units: unitless
- `.li.co.tif`: a COG with a single band containing Lunar Illuminance (LI) values
    - Data range: [0, inf)
    - No-data value: -1.0
    - Data type: floating point
    - Units: lux

The bounding box geometry of the area covered in each file is available in the metadata within the corresponding JSON file and in the COG itself.

**Table 2: Bit-flag field descriptions for OLS “flag” file**

| Flag Name | Flag Bit Position | Flag State Description |
| --- | --- | --- |
| OLS_CLOUD1 | 0 | This bit is set to 1 if the OLS pixel is determined to be a cloud given the primary (more restrictive) set of parameters on the OLS cloud algorithm. |
| OLS_LIGHT1 | 1 | This bit is set to 1 if the OLS pixel is determined to be a light given the primary (less restrictive) set of parameters on the OLS light filtering algorithm. |
| OLS_GLARE | 2 | This bit is set to 1 if the OLS pixel is determined to be in an area of the swath impacted by solar glare (stray light) as determined by the OLS glare algorithm. |
| OLS_BSL_AND_LIGHTNING | 3 | This bit is set to 1 if the OLS scanline is determined to contain lightning and/or is a bad scanline as determined by the OLS lightning algorithm. |
| OLS_PIXEL_CENTER | 4 | This bit is set to 1 if the grid cell is an exact match to the location of an OLS pixel center. |
| OLS_DAYTIME | 5 | This bit is set to 1 if the OLS pixel is collected in daytime conditions. This region is determined using solar elevation angles and defines an area where no nighttime lights can be seen. |
| OLS_NIGHTTIME_MARGINAL | 6 | This bit is set to 1 if the OLS pixel is determined to be in the transition zone between day and night, aka the “terminator”. This region is determined using solar elevation angles and defines an area where nighttime lights can be seen, but the background is starting to be impacted by the sun. |
| OLS_LIGHT2 | 7 | This bit is set to 1 if the OLS pixel is determined to be a light given the secondary (more restrictive) set of parameters on the OLS light filtering algorithm. |
| OLS_CLOUD2 | 10 | This bit is set to 1 if the OLS pixel is determined to be a cloud given the secondary (less restrictive) set of parameters on the OLS cloud algorithm. |
| OLS_ZERO_LUNAR_ILLUM | 11 | This bit is set to 1 if the OLS pixel is collected when no moonlight is present (lunar illuminance value < threshold). |
| OLS_FIXED_GAIN | 12 | This bit is set to 1 if the scanline was part of a special collection where the OLS gain setting was fixed. Normally the OLS gain is allowed to fluctuate given the collection’s environmental parameters. |
| OLS_CLOUDS_UNKNOWN | 13 | This bit is set to 1 if ancillary data needed to determine cloud state was not available. |
| OLS_NO_DATA | 15 | This bit is set to 1 if no data is available for that scanline/section of orbit, or the grid cell is outside the bounds of the swath. |

### VIIRS-DNB
VIIRS-DNB data are available starting in April of 2012. The data are organized by either the year-month in which the data were captured, or by satellite year-month starting in 2018. If there is no satellite name, the satellite is assumed to be NPP. For example:
- `s3://globalnightlight/201505/` contains all data for May 2015 with satellite NPP
- `s3://globalnightlight/npp_202012/` contains all data for December 2020 with satellite NPP

Within a given sub-directory, data are provided in ~6 minute orbital segments, or aggregates, for every day (night) of the given month. For each aggregate, there are 5 image layers and a JSON metadata file. For a given aggregate, these 6 files all have the similar file prefixes, which contain some metadata about the data layer, the time of data collect (UTC), orbit number, and creation time of the VIIRS sensor data record (SDR) when placed in the <a href="https://www.avl.class.noaa.gov/saa/products/welcome;jsessionid=D085DD932AA68DCA4BCB17F63559AE1A">NOAA CLASS archive</a>. These file prefixes follow the naming convention and structure of Sensor Data Records as described in the <a href="https://ncc.nesdis.noaa.gov/documents/documentation/viirs-users-guide-tech-report-142a-v1.3.pdf">VIIRS SDR User's Guide</a>, and are also described below.

The 6 filenames for the layers/metadata associated with a given aggregate time are shown by example:

- `SVDNB_npp_d20150504_t1335358_e1341162_b18219_c20150504194116381040_noaa_ops.rade9.co.tif`
- `SVDNB_npp_d20150504_t1335358_e1341162_b18219_c20150504194116381040_noaa_ops.rade9.co.json`
- `npp_d20150504_t1335358_e1341162_b18219.vflag.co.tif`
- `GDNBO_npp_d20150504_t1335358_e1341162_b18219_c20150504194116380812_noaa_ops.li.co.tif`
- `GDTCN_npp_d20150504_t1335358_e1341162_b18219_c20150504194116380812_noaa_ops.samples.co.tif`
- `SVM15_npp_d20150504_t1335358_e1341162_b18219_c20150504194116358997_noaa_ops.rad.co.tif`

For this aggregate time, each file contains common aggregate identification fields. In this example, the aggregate identifier common to each filename is:
```
npp_d20150504_t1335358_e1341162_b18219
npp -> satellite ID
    d20150504 -> start date of first scan in aggregate (2015/05/04)
              t1335358 -> time of first scan (13:35:35.8)
                       e1341162 -> time of last scan (13:41:16.2)
                                b18219 -> orbit number of first scan
```

All but one of the filenames are prepended with a product ID and have an additional timestamp or “creation time”. These will be described below, again using a filename prefix from our example aggregate:
```
SVDNB_npp_d20150504_t1335358_e1341162_b18219_c20150504194116381040_noaa_ops
SVDNB -> Day/Night Band SDR (all possible product IDs are listed below)
      npp_d20150504_t1335358_e1341162_b18219 -> aggregate identifier
                                             C20150504194116381040 -> creation date/time of SDR
                                                                   noaa -> data origin
                                                                        ops -> data domain
```

ALL possible product IDs in this repository: 

- `SVDNB` -> Day/Night Band SDR
- `GDNBO` -> Day/Night Band Geolocation
- `GDTCN` -> Day/Night Band Geolocation. This is NCEI’s internal terrain corrected version before it was available in the standard VIIRS DNB geolocation product.
- `SVM15` -> Moderate Resolution band 15 SDR (longwave thermal)

The VIIRS layers can be further distinguished by their file extensions:

- `.rade9.co.tif`: a COG with a single band containing the DNB nighttime radiance (this is the key data file)
  - Data range: (-1.5, inf)
  - “No-data” values: -999.3 and -1.5
  - Data type: floating point
  - Units: nanowatts/cm<sup>2</sup>/sr
- `.rade9.co.json`: a JSON file following the STAC schema with metadata for the nighttime radiance data, including a timestamp and a geospatial bounding box
- `.vflag.co.tif`: a COG with a single band containing bitflags that can be queried for data quality
  - Data range: [0, 2<sup>31</sup>-1]
  - “No-data” value: 2<sup>31</sup>
  - Bit-fields: see Table 3
  - Data type: 32-bit integer
  - Units: Unitless
- `.rad.co.tif`: a COG with a single band containing the TIR radiance
  - Data range:
  - “No-data” value: -999.3
  - Data type: floating point
  - Units: W m<sup>-2</sup> sr<sup>-1</sup> μm<sup>-1</sup>
- `.samples.co.tif`: a COG with a single band containing sample position for the DNB pixels along the swath.
  - Data range: [1, 4064]
  - No-data value: 0
  - Data type: 16-bit integer
  - Units: unitless
- `.li.co.tif`: a COG with a single band containing Lunar Illuminance (LI) values
  - Data range: [0, inf)
  - No-data value: -999.3
  - Data type: floating point
  - Units: lux

**Table 3: Bit-flag field descriptions for DNB “vflag” file**

| Flag Name | Flag Bit Position | Flag State Description |
| --- | --- | --- |
| VIIRS_CLOUD_QC | 2 | This bit is set to 1 if the VIIRS cloud algorithm results should be considered of poor quality (e.g. not enough ancillary data for the algorithm to give confident results.) |
| VIIRS_CLOUD | 3-4 | This 2-bit field has the following values: (0) Clear sky; (1) Probably cloudy; (2) Confidently cloudy; (3) Clouds unknown. These values are taken from the VIIRS Cloud Mask (VCM) Environmental Data Record (EDR)  through 2017 and then the <a href="https://www.star.nesdis.noaa.gov/jpss/clouds.php">VIIRS Enterprise Cloud Mask (ECM)</a> product from 2018 forward. |
| VIIRS_ZERO_LUNAR_ILLUM | 5 | This bit is set to 1 if the VIIRS-DNB pixel is collected when no moonlight is present (lunar illuminance value < threshold). |
| VIIRS_DAY_NIGHT_TERM | 6-7 | This 2-bit field has the following values: (0) Day - grid cell is in daytime conditions; (1) Terminator - grid cell is in terminator zone (transition region between day and night); (2) Night - grid cell is in nighttime conditions; (3) Unknown. These regions are determined using solar elevation angles. |
| VIIRS_STRAY_LIGHT | 14-15 | This 2-bit field has the following values: (0) NO stray light impact; (1) Stray light impact region (per solar elevation model); (2) Stray light correction algorithm run on DNB; (3) Stray light impact region AND stray light correction run on DNB. Note: stray light correction began on the VIIRS DNB SDR imagery in 2014. |
| VIIRS_DNB_LIGHTNING | 22-23 | This 2-bit field has the following values: (0) No lightning detected; (1) Lightning signature detected; (2) Spare value; (3) No data OR lightning algorithm did not execute. |
| VIIRS_DNB_HEP | 24 | This bit is set to 1 if the DNB pixel is determined to contain a High-Energy particle hit per internal algorithm (common in the South Atlantic Anomaly zone over South America). |
| VIIRS_NO_DATA | 31 | This bit is set to 1 if no data is available for that scanline/section of orbit, or the grid cell is outside the bounds of the swath. |

---
<a href="http://aws.amazon.com/opendata/public-datasets">AWS Public Datasets</a>