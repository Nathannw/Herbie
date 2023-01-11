## Added by Brian Blaylock
## July 26, 2021


class gdas:
    def template(self):
        self.DESCRIPTION = "Global Data Assimilation System"
        self.DETAILS = {
            "nomads product description": "https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GDAS",
            "google cloud platform": "https://console.cloud.google.com/marketplace/product/noaa-public/gfs?q=search&referrer=search&project=python-232920",
            "azure document": "https://github.com/microsoft/AIforEarthDatasets#noaa-global-forecast-system-gfs",
            "aws document": "https://registry.opendata.aws/noaa-gfs-bdp-pds",
        }
        self.PRODUCTS = {
            "atmos.25": "common fields, 0.25 degree resolution",
            "atmos1": "common fields, 1.00 degree resolution",
        }

        products = {
            "atmos.25": "pgrb2.0p25",
            "atmos1": "pgrb2.1p00",
        }
        # Get *actual* name of GDAS product.
        self.product = products.get(self.product)

        filedir = f"gdas.{self.date:%Y%m%d/%H}/atmos}"
        filename = f"gdas.t{self.date:%H}z.{self.product}.f{self.fxx:03d}"
        filepath = f"{filedir}/{filename}"

        self.SOURCES = {
            "aws": f"https://noaa-gfs-bdp-pds.s3.amazonaws.com/{filepath}",
            "aws-old": f"https://noaa-gfs-bdp-pds.s3.amazonaws.com/gdas.{self.date:%Y%m%d/%H}/{filename}",
            "ftpprd": f"https://ftpprd.ncep.noaa.gov/data/nccf/com/gfs/prod/{filepath}",
            "nomads": f"https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/{filepath}",
            "google": f"https://storage.googleapis.com/global-forecast-system/{filepath}",
            "azure": f"https://noaagfs.blob.core.windows.net/gfs/{filepath}",
        }
        self.IDX_SUFFIX = [".idx"]
        self.LOCALFILE = f"{self.get_remoteFileName}"


class gfs:
    def template(self):
        self.DESCRIPTION = "Global Forecast System"
        self.DETAILS = {
            "nomads product description": "https://www.nco.ncep.noaa.gov/pmb/products/gfs",
            "google cloud platform": "https://console.cloud.google.com/marketplace/product/noaa-public/gfs?q=search&referrer=search&project=python-232920",
            "azure document": "https://github.com/microsoft/AIforEarthDatasets#noaa-global-forecast-system-gfs",
            "aws document": "https://registry.opendata.aws/noaa-gfs-bdp-pds",
        }
        # I want the product names to be simplified.
        self.PRODUCTS = {
            "atmos.25": "common fields, 0.25 degree resolution",
            "atmos.5": "common fields, 0.50 degree resolution",
            "atmos1": "common fields, 1.00 degree resolution",
            "atmos.25b": "uncommon fields, 0.25 degree resolution",
            "atmos.5b": "uncommon fields, 0.50 degree resolution",
            "atmos1b": "uncommon fields, 1.00 degree resolution",
            "atmos.5_full": "combined grids of 0.50 resolution",
        }

        products = {
            "atmos.25": "pgrb2.0p25",
            "atmos.5": "pgrb2.0p50",
            "atmos1": "pgrb2.1p00",
            "atmos.25": "pgrb2b.0p25",
            "atmos.5b": "pgrb2b.0p50",
            "atmos1b": "pgrb2b.1p00",
            "atmos.5_full": "pgrb2full.0p50",
        }
        # Get *actual* name of GFS product.
        self.product = products.get(self.product)

        filedir = f"gfs.{self.date:%Y%m%d/%H}/atmos}"
        filename = f"gfs.t{self.date:%H}z.{self.product}.f{self.fxx:03d}"
        filepath = f"{filedir}/{filename}"

        self.SOURCES = {
            "aws": f"https://noaa-gfs-bdp-pds.s3.amazonaws.com/{filepath}",
            "aws-old": f"https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.{self.date:%Y%m%d/%H}/{filename}",
            "ftpprd": f"https://ftpprd.ncep.noaa.gov/data/nccf/com/gfs/prod/{filepath}",
            "nomads": f"https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/{filepath}",
            "google": f"https://storage.googleapis.com/global-forecast-system/{filepath}",
            "azure": f"https://noaagfs.blob.core.windows.net/gfs/{filepath}",
        }
        self.IDX_SUFFIX = [".idx"]
        self.LOCALFILE = f"{self.get_remoteFileName}"

#TODO: consolidate this into GFS model, and use product names "wave.arctic", "wave.25", etc.
class gfs_wave:
    def template(self):
        self.DESCRIPTION = "Global Forecast System - Wave Products"
        self.DETAILS = {
            "nomads product description": "https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GFSwave",
        }
        self.PRODUCTS = {
            "arctic.9km": "Arctic; 9-km resolution",
            "atlocn.0p16": "North Atlantic 0.16 deg resolution",
            "epacif.0p16": "Eastern Pacific; .16 deg resolution",
            "global.0p16": "Global; 0.16 deg resolution",
            "global.0p25": "Global; 0.25 deg resolution",
            "gsouth.0p25": "Global South; 0.25 deg resolution",
            "wcoast.0p16": "West Coast; 0.16 deg resolution",
        }
        self.SOURCES = {
            "aws": f"https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.{self.date:%Y%m%d/%H}/wave/gridded/gfswave.t{self.date:%H}z.{self.product}.f{self.fxx:03d}.grib2",
            "ftpprd": f"https://ftpprd.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.{self.date:%Y%m%d/%H}/wave/gridder/gfswave.t{self.date:%H}z.{self.product}.f{self.fxx:03d}.grib2",
            "nomads": f"https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.{self.date:%Y%m%d/%H}/wave/gridded/gfswave.t{self.date:%H}z.{self.product}.f{self.fxx:03d}.grib2",
            "google": f"https://storage.googleapis.com/global-forecast-system/gfs.{self.date:%Y%m%d/%H}/wave/gridded/gfswave.t{self.date:%H}z.{self.product}.f{self.fxx:03d}.grib2",
            "azure": f"https://noaahrrr.blob.core.windows.net/gfs/gfs.{self.date:%Y%m%d/%H}/wave/gridded/gfswave.t{self.date:%H}z.{self.product}.f{self.fxx:03d}.grib2",
        }
        self.LOCALFILE = f"{self.get_remoteFileName}"
