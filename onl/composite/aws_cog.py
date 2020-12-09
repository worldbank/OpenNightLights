import boto3
from osgeo import gdal

# s3 = boto3.resource('s3')
# obj = s3.Object(bucket, key)
# body = obj.get()['Body'].read()

testtiff = "/vsicurl/http://even.rouault.free.fr/gtiff_test/S2A_MSIL1C_20170102T111442_N0204_R137_T30TXT_20170102T111441_TCI_regular_with_ovr_2.tif"
testvirrs = "/vsicurl/https://globalnightlight.s3.amazonaws.com/201712/SVDNB_npp_d20171201_t0000497_e0006301_b31576_c20171201060630477360_nobc_ops.rade9.co.tif"


# gdal
# data = gdal.Open(path)
# info = gdal.Info(path)

# get the bounding box of an area
# gdal_translate
# - proj_win (in pixels)
# gdal.Translate('out.tif', testvirrs, wid


# gdalwarp
# -te  georeferenced extents of output file