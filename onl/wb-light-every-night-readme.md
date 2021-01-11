## World Bank - Light Every Night data archive documentation
World Bank Light Every Night is a comprehensive data archive of nighttime light collected from two sensors over the last three decades: the Defense Meteorological Satellite Program (DMSP) Operational Line-Scan System (OLS) with data from 1992-2017, and the Visible Infrared Imaging Radiometer Suite (VIIRS) Day-Night Band (DNB) with data spanning 2012-2020. The underlying data are sourced from the National Oceanic and Atmospheric Administration (NOAA)/ National Centers for Environmental Information (NCEI) archive.

The DMSP-OLS and VIIRS-DNB sensors capture various sources of low-light emissions from Earth. These include sources that indicate aspects of human activity, like city lights, gas flares, fishing boats, and agricultural fires, while also capturing other nighttime lights phenomena such as auroras.

The World Bank worked in collaboration with NOAA/NCEI and the University of Michigan to publish this archive, designed from the ground up to be analysis-ready. The data are published in Cloud Optimized GeoTIFF format (COG), and organized using the Spatial Temporal Asset Catalog (STAC) standard. These standards are part of the growing Analysis Ready Data ecosystem that is improving access to geospatial data sets, enabling broader audiences to readily discover, process and analyze geospatial data. Analysis ready data has already undergone the transformations and preprocessing necessary to make data (in this case observations of electromagnetic energy collected in space!) organized and coherent for general technical users and analysts.

Learn more about how remote sensing, nighttime light images and using these data for analysis at the <a href="https://worldbank.github.io/OpenNightLights/welcome.html">World Bank's Open Nighttime Lights tutorial</a>.

Accessing Landsat on AWS
The data are organized using a directory structure based on each scene’s path and row. For instance, the files for Landsat scene LC08_L1TP_139045_20170304_20170316_01_T1 are available in the following location: s3://landsat-pds/c1/L8/139/045/LC08_L1TP_139045_20170304_20170316_01_T1/

The “c1” refers to Collection 1, the “L8” refers to Landsat 8, “139” refers to the scene’s path, “045” refers to the scene’s row, and the final directory matches the product’s identifier, which uses the following naming convention: LXSS_LLLL_PPPRRR_YYYYMMDD_yyymmdd_CC_TX, in which:

- L = Landsat
- X = Sensor
- SS = Satellite
- PPP = WRS path
RRR = WRS row

Each scene’s directory includes:

a .TIF GeoTIFF for each of the scene’s up to 12 bands (note that the GeoTIFFs include 512x512 internal tiling)
.TIF.ovr overview file for each .TIF (useful in GDAL based applications)
a _MTL.txt metadata file
a small rgb preview jpeg, 3 percent of the original size
a larger rgb preview jpeg, 15 percent of the original size
an index.html file that can be viewed in a browser to see the RGB preview and links to the GeoTIFFs and metadata files
For instance, the files associated with scene LC08_L1TP_139045_20170304_20170316_01_T1 are available at:

s3://landsat-pds/c1/L8/139/045/LC08_L1TP_139045_20170304_20170316_01_T1/

or

https://landsat-pds.s3.amazonaws.com/c1/L8/139/045/LC08_L1TP_139045_20170304_20170316_01_T1/index.html

A gzipped csv describing all available scenes is available at

s3://landsat-pds/scene_list.gz

or

https://landsat-pds.s3.amazonaws.com/c1/L8/scene_list.gz

If you use the AWS Command Line Interface, you can access the bucket with this simple command:

aws s3 ls landsat-pds/c1/

Note that Collection 1 Real-Time data will be stored on a rolling, 1 month basis to be backfilled as Tier 1 data becomes available.