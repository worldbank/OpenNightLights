# World Bank - Light Every Night

<p></p>

<p>World Bank Light Every Night is a comprehensive data archive of nighttime light collected from two sensors over the last three decades: the Defense Meteorological Satellite Program (DMSP) Operational Line-Scan System (OLS) with data from 1992-2017, and the Visible Infrared Imaging Radiometer Suite (VIIRS) Day-Night Band (DNB) with data spanning 2012-2020.</p>

<p>The DMSP-OLS and VIIRS-DNB sensors capture various sources of low-light emissions from Earth. These include sources that indicate aspects of human activity, like city lights, gas flares, fishing boats, and agricultural fires, while also capturing other nighttime lights phenomena such as auroras.</p>

<p>The World Bank worked in collaboration with the National Oceanic and Atmospheric Administration (NOAA) and the University of Michigan to publish this archive, designed from the ground up to be analysis-ready. The underlying data are sourced from the NOAA National Centers for Environmental Information (NCEI) archive. Additional processing by the University of Michigan enables access in Cloud Optimized GeoTIFF format (COG) and search using the Spatial Temporal Asset Catalog (STAC) standard. These standards are part of the growing Analysis Ready Data ecosystem that is improving access to geospatial data sets, enabling broader audiences to readily discover, process and analyze geospatial data.</p>

<p>Learn more about remote sensing, nighttime light images and using these data for analysis at <a href="https://worldbank.github.io/OpenNightLights/welcome.html">World Bank's Open Nighttime Lights tutorial</a>.</p>

<h2 id="wb-len-data-structure">Light Every Night file structure</h2>

<p>The data for both DMSP-OLS and VIIRS-DNB are in the root AWS S3 bucket,  <code>s3://globalnightlight/</code>. DMSP-OLS data are organized by satellite name and year and VIIRS-DNB are organized by month.</p>

<h3 id="accessing-dmsp">DMSP-OLS</h3>

<p>DMSP-OLS data are organized by satellite name and year data were captured. <a href="https://eogdata.mines.edu/dmsp/downloadV4composites.html">This website</a> provides a table of DMSP satellite name and year pairs through 2013. For example, <code>s3://globalnightlight/F121995/</code>, contains all data collected by satellite F12 in the year 1995.</p>

<p>Within a given sub-directory, data are provided by satellite orbit for every day (night) of the given year. The key files are those with the .vis.co.tif extension, which contain the nighttime visible band data (and a supplemental JSON file with metadata on this .vis.co.tif file), and those with the .flag.co.tif extension, which contain data quality masks for several fields:</p>
<ul>
<li><code>.vis.co.tif</code>: a COG with a single band containing the visible nighttime imagery (this is the key data file)</li>
<li><code>.vis.co.json</code>: a JSON file following the STAC schema with metadata for the VIS file, including a timestamp and a geospatial bounding box</li>
<li><code>.flag.co.tif</code>: a COG with a single band containing a bitflag for data quality</li>
</ul>

<p>There are additional files that contain the co data:</p>
<ul>
<li><code>.tir.co.tif</code>: a COG with a single band containing Thermal Infrared (TIR) data</li>
<li><code>.li.co.tif</code>: a COG with a single band containing Lunar Illuminance (LI) </li>
<li><code>.samples.co.tif</code>: a COG with a single band containing samples</li>
</ul>

<p>In every case, the stem of the filename corresponds with the satellite name, year, date and time (in UTC) of data collection. For example <code>F12199501010014.night.OIS.vis.co.tif</code> contains the visible nighttime imagery collected from the satellite F12 in 1995, on January 1, at 00 hours and 14 minutes. The bounding box geometry of the area covered in the file is available in the metadata within the corresponding JSON file and in the COG itself.</p>

<h3 id="accessing-viirs">VIIRS-DNB</h3>

<p>VIIRS-DNB data are organized by the year-month the data were captured. For example <code>s3://globalnightlight/201505/</code> contains all data collected in May of 2015.</p>

<p>As with DMSP-OLS, within a given sub-directory, data are provided for every day (night) of the given year. These files follow the naming convention and structure of Sensor Data Records as described in the <a href="https://ncc.nesdis.noaa.gov/documents/documentation/viirs-users-guide-tech-report-142a-v1.3.pdf">VIIRS SDR User's Guide</a>.</p>

<p>For example, the naming convention for the file: <code>SVDNB_npp_d20150504_t1335358_e1341162_b18219_c20150504194116381040_noaa_ops.rade9.co.tif</code> is:</p>
<ul>
<li><code>SVDNB</code>: prefix/product id (e.g. "SVDNB" for Sensor Data Record of Day-Night Band data)</li>
<li><code>npp</code>: satellite (e.g. npp for Suomi National Polar-orbiting Partnership)</li>
<li><code>d20150504</code>: date of data capture (e.g. d20150504 for May the 4th 2015)</li>
<li><code>t1335358</code>: time of the scan start (e.g. t1335358 for hour:13, minute:35, millisecond:358)</li>
<li><code>e1341162</code>: time of the scan end (e.g. e1341162 for hour:13, minute:41, millisecond:162)</li>
<li><code>b18219</code>: the orbit number (e.g. b18219 orbit # 18219)</li>
<li><code>c20150504194116381040</code>: the file creation date/time (e.g. c20150504194116381040 for May the 4th 2015, hour:19 minute:41 and 16381040 x 10<sup>-8</sup> seconds)</li>
<li><code>noaa_ops</code>: the origin (e.g. noaa_ops for NOAA)</li>
<li><code>rade9.co.tif</code>: an extension indicating data type (e.g. rade9.co.tif for Cloud-Optimized GeoTiff of nighttime radiance)</li>
</ul>
<p>As with the DMSP data, there are several files containing different data. The key files are those with the <code>.rade9.co.tif</code> extension, which contain the nighttime radiance data (and a supplemental JSON file with metadata on this file), and those with the <code>.vflag.co.tif</code> extension, which contain data quality masks for several fields. These files are as follows:</p>

<ul>
<li><code>.rade9.co.tif</code>: a COG with a single band containing a visible nighttime radiance (this is the key data file)</li>
<li><code>.rade9.co.json</code>: a JSON file with metadata for the nighttime radiance data, including a timestamp and a geospatial bounding box</li>
<li><code>.vflag.co.tif</code>: a COG with a single band containing a bitflag for data quality</li>
<li>Prefix <code>SVM16</code> and extension <code>.rad.co.tif</code>: a COG with a single band containing a visible image data from the VIIRS M16 band</li>
</ul>

<p>There are additional files that contain reference data:</p>
<ul>
<li><code>.li.co.tif</code>: a COG with a single band containing Lunar Illuminance (LI) </li>
<li><code>.samples.co.tif</code>: a COG with a single band containing samples</li>
</ul>

<h2 id="accessing-data-aws">Accessing Light Every Night data on AWS</h2>

<p>You can access these data via the link, <code>s3://globalnightligh</code> and using the web interface via the AWS console. Or via the AWS Command Line Interface, for example to list all files in the VIIRS 201505 sub-directory, using the <code>--no-sign-request</code> flag since this bucket is public:</p>

<p><code>aws s3 ls s3://globalnightlight/201505 --no-sign-request</code></p>

---
<a href="http://aws.amazon.com/opendata/public-datasets">AWS Public Datasets</a>
