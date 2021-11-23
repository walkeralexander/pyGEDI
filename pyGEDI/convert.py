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

    if os.path.exists(csv_file):
        try:
            os.makedirs(outdir)
        except:
            print ("Successfully created")   
        comand= ['ogr2ogr','-oo','X_POSSIBLE_NAMES=lon*','-oo','Y_POSSIBLE_NAMES=lat*','-f','ESRI Shapefile','-wrapdateline','-t_srs','EPSG:4326','-s_srs','EPSG:4326',outdir+filename+'.shp',csv_file]
        subprocess.Popen(comand) 
        return 'File successfully converted.'
    else:
        return 'CSV file does not exist'
    
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


