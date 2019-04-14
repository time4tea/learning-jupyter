import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

import requests
import zipfile

shape_url = "https://opendata.arcgis.com/datasets/d5c9c1d89a5a44e9a7f88f182ffe5ba2_2.zip?outSR=%7B%22latestWkid%22%3A27700%2C%22wkid%22%3A27700%7D"
shape_zip = "/tmp/shape.zip"
shape_local = "/tmp/Wards_December_2016_Generalised_Clipped_Boundaries_in_the_UK.shp"

import shutil
import os

def download(url, local):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(local, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)    
    print(f"Downloaded {url}")

if os.path.exists(shape_local):
    os.unlink(shape_local)

if not os.path.exists(shape_local):
    download(shape_url, shape_zip)
    with zipfile.ZipFile(shape_zip) as myzip:
        myzip.extractall("/tmp")

map_frame = gpd.read_file(shape_local)


# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

map_frame.plot(ax = ax)

# remove the axis
ax.axis('off')

