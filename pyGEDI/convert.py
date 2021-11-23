import os
import subprocess
import logging
import pandas as pd


def make_dir(outdir: str) -> None:
    """Make the directory and log if exists.

    Args:
        outdir (str): the directory to create.
    """
    try:
        os.makedirs(outdir)
    except FileExistsError:
        logging.info('Directory {outdir} already exists.')
    df.to_csv(outdir+filename+'.csv', index=False, header=True)  
    return 'DataFrame successfully converted.'


def df2csv(df: pd.DataFrame, filename: str, outdir: str) -> None:
    """Save the dataframe to a file.

    Args:
        df (pd.DataFrame): the dataframe to save out.
        filename (str): the filename to save dataframe at.
        outdir (str): the directory to save the dataframe in.
    """
    make_dir(outdir)
    df.to_csv(f'{outdir}/{filename}.csv', index=False, header=True)


def csv2shp(csv_file: str, filename: str, outdir: str) -> None:
    """Convert a csv to a shp file.

    Args:
        csv_file (str): the path to the csv file to convert.
        filename (str): the filename to save the converted shp to.
        outdir (str): the directory to save the shp file in.
    """
    make_dir(outdir)
    if os.path.exists(csv_file):
        cmd = [
            'ogr2ogr',
            '-oo', 'X_POSSIBLE_NAMES=lon*',
            '-oo', 'Y_POSSIBLE_NAMES=lat*',
            '-f', 'ESRI Shapefile',
            '-wrapdateline',
            '-t_srs', 'EPSG:4326',
            '-s_srs', 'EPSG:4326',
            f'{outdir}/{filename}.shp',
            csv_file
        ]
        subprocess.Popen(cmd)
    else:
        raise FileNotFoundError(f'File {csv_file} not found.')

def shp2tiff(shp_file, layername, pixelsize, nodata, ot, filename,outdir):
    if os.path.exists(shp_file):
        try:
            os.makedirs(outdir)
        except:
            print ("Successfully created")   
        comand=['gdal_rasterize','-tr',pixelsize,pixelsize,'-a_nodata',nodata,'-ot',ot,'-of','GTiff','-co','COMPRESS=LZW','-a',layername,shp_file,outdir+filename+'.tif']
        subprocess.Popen(comand)
        return 'File successfully converted.'

    else:
        return 'SHP file does not exist'


