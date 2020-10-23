#  25 years of DMSP-OLS and VIIRS archive: data structure, format  and access (10 min)

In this module, we want to give you a little more specific information 
about the data we’ll be working with. First, it’s helpful to understand 
the basic data formats that are used with geospatial data analysis.

[NOTE: this section is a WIP as the data are added to S3 by U.Mich team 
and NOAA. As soon as a full sample of the data added to S3 and in their 
final structure, we can add information on that here.]

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

**In this course:** The data we are accessing from DMSP-OLS and VIIRS-DNB have been stored as COGs.

## Amazon Web Services (AWS)
Data we’re working with come from the DMSP-OLS archive and from the VIIRS-DNB instrument, 
which is still collecting data. Since these data files are large and the numbers grow each 
month as data are collected, it is useful to store and manage these files with a cloud service. 
We already introduced you to Google Earth Engine, one such cloud provider. 
We are also using Amazon Web Service (AWS) to store our own data files directly.

<div class="alert alert-info">
<b>AWS</b>  is a subsidiary of Amazon and provides a wide range of cloud services, 
including data storage and computing.</div>

We’ll mostly be leveraging AWS’s Simple Storage Service, S3.

<div class="alert alert-success">
<a href="https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html" 
class="alert-link">Here’s a guide</a> that explains AWS S3 data storage and walks through 
how to set up an AWS account.
</div>

[NOTE: how we serve these COGs is still an open question. We could just give access to the 
S3 bucket, but that would require users to set up AWS accounts and learn S3...might be too much. 
I’m also not sure we’d be leveraging the advantage of COGs by doing that 
(users would have to download the entire files anyway). Better to use a tool to query 
these COGs and then here we can just instruct users how to do so. But can we leverage an 
existing tool or need to build a new one? Not a trivial amt of work either way, so we’ll 
want to update this section accordingly. For now, we’ll just describe the structure of the 
data files but need to sort this out.]

## Nighttime Light Data structure and organization

[TO DO: When data are uploaded, insert a description of the file structure].

### DMSP-OLS

[TO DO: We need to complete this section once we’ve added sample data].

### VIIRS-DNB

[TO DO: We need to complete this section once we’ve added sample data. For example, 
in addition to the radiance values, there are other layers and metadata, 
such as the cloud mask. These will ideally be added to the COG structure so they can be 
queried, but we need to finalize this].

**VIIRS-DNB data basics**

<div class="alert alert-success">
The following <a href="http://rammb.cira.colostate.edu/projects/npp/Beginner_Guide_to_VIIRS_Imagery_Data.pdf" 
class="alert-link">beginners guide</a> is helpful for those looking for more detail on the data.
</div>

Here are just a few highlights:

As the satellite orbits the Earth, VIIRS scans a swath that is ~3040 km wide 
(the “cross-track direction” which is perpendicular to the direction the satellite is moving) 
and 12 km in the “along-track” direction. 

A rotating mirror collects data for the various detectors, including the Day/Night Band (DNB) 
that we are using for nighttime lights. One rotation of the mirror is one scan.

48 of these scans are put together into a single “granule” of data, 
so that this represents about 3040 km by 570 km (48 * 12km) or surface area data 
collected over about 85 seconds.

The data that comes from the satellite is transmitted to Earth as a Raw Data Record (RDR). 
Most users will never see this data; however. These RDR files are calibrated. 
For example, georeferencing information is added and the raw “counts” of photons 
collected are converted to a measure, like radiance or reflection. These are known as 
Sensor Data Records (SDRs) and are commonly referred to as “raw” 
(even if they are not technically RDRs) or “un-adjusted” files.

**VIIRS source data**

The main VIIRS-DNB data files are COGs that are structured like these SDRs. 
They include the values for radiance (i.e. nighttime lights) as well as other important 
meta-data, including pixel data quality and cloud coverage.

TO DO: detailed description of data and meta-data structure when data are added/completed]

These  files follow the naming convention used for SDRs. 
That naming structure tells you helpful information about what the data are and when they 
were collected.

For example:
```{figure} img/mod1-viirs_datafile.png
---
name: viirs-datafile
---
```
**Accessing the data**
Later in this tutorial, we explore how to access these data files, 
but hopefully this gives you a general sense of where the data come from and 
how they’re structured. One of the exciting things about working with remote sensing 
data is that we’re investigating information that started as pure energy: a photon 
collected in space. This information makes its journey to a data file you can analyze or 
display in a map so that we can learn a little more about what’s happening on Earth!

## References:
```{bibliography} ../references.bib
:filter: docname in docnames
```