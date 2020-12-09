#  Data overview (10 min)

In this module, we want to give you a little more specific information 
about the data we’ll be working with. First, it’s helpful to understand 
the basic data formats that are used with geospatial data analysis.

## Data Structure
**Raster vs. Vector data**

Geospatial data from the “real world” can be stored in different types 
of formats or data types: In this course we will be working with two 
types of geospatial data stored as either a **raster** or a **vector** format.

### Raster files
<div class="alert alert-info">
Data stored in a <b>raster format</b> is arranged in a regular grid of cells, 
without storing the coordinates of each point (namely, a cell, or a pixel). 
The coordinates of the corner points and the spacing of the grid can 
be used to calculate (rather than to store) the coordinates of each 
location in the grid. Any given pixel in the grid stores one or more 
values (in one or more bands).</div> 

A satellite image, an image you take with your camera or even a map layer
you are looking at can be examples of geospatial data that are stored in a 
raster format. These images are composed of pixels that are organized in 
rows and columns, with values and location. The size of a given pixel 
depends on the spatial resolution of the sensor. 

Raster files are often composed out of multiple bands (channels). 
Each band represents, for example, the amount of electromagnetic 
radiation reflected from the surface on Earth 
along multiple regions of the electromagnetic spectrum.

Raster data is typically used to represent continuous surfaces, 
where knowing the exact boundaries in high precision is of less importance. 

### Vector files
<div class="alert alert-info">
Data in a <b>vector format</b> is stored in a way that the X and Y 
coordinates are stored for each point. Data can be represented, 
for example, as points, lines and polygons. A point has only one coordinate 
(X and Y), a line has two coordinates (at the start and end of the line) 
and an area is essentially a line that closes on itself to enclose a region. 
Polygons are usually used to represent the area and perimeter of a 
continuous geographic features. Vector data stores features in their 
original resolution, without aggregation.</div>

### Brief comparison of raster vs vector data models

```{figure} img/mod1-rastervector1.png
---
name: rastervector1
---
```
```{figure} img/mod1-rastervector2.png
---
name: rastervector2
---
Source: {cite}`joseph2014`
```

### GeoTIFFs
<div class="alert alert-info">
A <b>tagged Image File Format (TIFF or TIF)</b> is a file format for storing raster files. 
A GeoTIFF is a TIFF file that follows a specific standard for structuring meta-data, 
such as georeference information (e.g. map coordinates) for the image. Most of the 
remote sensing data you encounter will be stored as a GeoTIFF file and we will explore to 
read these files later in the tutorial.</div>

The meta-data stored in a TIFF is called a `tif tag` and GeoTIFFs often contain tags including:
1. **Spatial extent:** what is the area coverage of this file?
2. **Coordinate reference system:** what projection / coordinate reference system is used?
3. **Resolution:** rasters contain pixels, so what is the spatial extent of each pixel (spatial resolution)?
4. **Number of layers:** how many layers or bands are in the file?

<div class="alert alert-success">
<a href="https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/intro-to-the-geotiff-file-format/" 
class="alert-link">This tutorial at earthdatascience.org</a> gives a good overview of GeoTIFFs as well as the libraries,
such as Python's rasterio that are useful for accessing and manipulating this files.
</div>

<div class="alert alert-success">
<a href="https://rasterio.readthedocs.io/en/latest/#" 
class="alert-link">Rasterio</a> a Python library for reading and writing GeoTIFF files.
</div>


### Cloud-optimized geoTIFFs (COGs)
<div class="alert alert-info">
<b>Cloud Optimized GeoTIFFS (COGs)</b>  are GeoTIFFs that have data structured in such a 
way that you can query these files through a web service. The major advantage of this is 
that you can query, analyze, visualize, or download just a part of a COG file online, 
without downloading the entire file.
</div>

It’s often the case with remote sensing analysis that you only need to view or analyze a 
particular area and the data that contains that area is in a very large file that contains a 
much larger region of the world. COGs allow you to query just the area that you’re interested 
in, saving you time and storage space.

## The World Bank's "Light Every Night" dataset

Currently, this tutorial focuses on nighttime lights datasets that are available publicly (via the Google Earth Engine data catalogue); however, the "Light Every Night" (LEN) data archive is going to be launched soon. 

The World Bank’s Light Every Night data set is a complete archive of all nighttime imagery captured each night over the last three decades. The underlying data is sourced from the NOAA/NCEI archive. The two sensors featured are the DMSP-OLS with data from 1992-2017, and the VIIRS-DNB with data spanning 2012-2020. The World Bank worked in collaboration with NOAA/NCEI and the University of Michigan to publish the archive as an Analysis Ready Data Set. The LEN archive, which now spans nearly 250 terabytes, will be openly available on the AWS open data program published under the World Bank’s open data license.

### Components of the LEN archive

- DMSP-OLS nightly imagery (1993-2017, all nights):
    - visible (VIS)
    - thermal infrared (TIR)
    - lunar illuminance (LI)
    - cloud mask (CM)
    - sample position (SAM)
    - stray light mask (SLM)

- VIIRS DNB nightly imagery (2012-2020, all nights):
    - DNB radiance
    - I5 (LWIR) radiance
    - lunar illuminance
    - sample position within DNB scan
    - quality bitflag or "vflag" grid with on/off states for these fields:
    - daytime/nighttime/near-terminator
    - zero lunar illuminance
    - viirs cloud mask
    - nightfire detection
    - lightning
    - high energy particle hit
    - stray light affected/corrected

### Data that is "analysis ready"

The data architecture was designed from the ground up to be analysis-ready. The data is published in the Cloud Optimized GeoTIFF format (COG), and organized using the SpatialTemporal Asset Catalog (STAC) standard. These standards are part of the growing <a href="https://medium.com/planet-stories/analysis-ready-data-defined-5694f6f48815">Analysis Ready Data ecosystem</a> that is improving access to geospatial data sets, enabling broader audiences to readily discover, process and analyze geospatial data. 

Analysis ready data has already undergone the transformations and preprocessing necessary to make data (in this case observations of electromagnetic energy collected in space!) organized and coherent for general technical users and analysts.

### Data access and tutorials

This archive will be made available very shortly and soon thereafter, we will add more content to these modules about how to access and use this data.


## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```