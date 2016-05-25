# db_data

## Description of Data

This corpus contains the overlapping data from the [Million Song Dataset (MSD)](http://labrosa.ee.columbia.edu/millionsong/), [musiXmatch dataset](http://labrosa.ee.columbia.edu/millionsong/musixmatch), and [Tagtraum datasets](http://www.tagtraum.com/msd_genre_datasets.html). In order to achieve this we identified track IDs that existed in all three. This left a dataset size of roughly 1200 songs. The overall goal was to provide a dataset that was database independent so everyone can easily access this subset. 

otherdata.csv: Information from Tagtraum and MXM. Note genre field may contain two values. | symbol separates genres and words. detailed Headers: track_id, genre|genre, word|count

subset/: Information from MSD. Includes song data information such as artist name, song name, ect.  

common_songs.txt: Track IDs that intersect between MXM and Tagtraum datasets. 

msd_tagtraum_cd2.cls: Tagtraum data

geography/: Python/R code and data for geography clustering

- otherdata.csv: Information from Tagtraum and MXM.
- subset/: Information from MSD
- common_songs.txt: Overlap between MXM and Tagtraum datasets
- msd_tagtraum_cd2.cls: Tagtraum data
- geography/: All codes and data for geographical clustering 

## Scripts

extract_data.py: Python script that extracts the overlapping data between MSD, MXM, and Tagtraum datasets. This is how the csv was generated. Task: Read in data from the datasets, find the intersecting data, convert data into csv format.

/geography/extract_geography_data.py: extracts geographical data(track_id, artist_location, artist_latitude, artist_longitude) from MSD. The result files are geo_information.csv, geo_information_nan.csv(sub-dataset which has no coordinates), and geo_information_coordinates.csv(sub-dataset which has coordinates).

/geography/convert_nan_coordinates.py: gets latitude and longitude of the location in a geo_information_nan.csv file by using geocode. The output file is geo_information_nan_location_coordinates.csv.

/geography/geo_display.py: display coordinates of geo_information_coordinates.csv and geo_information_nan_location_coordinates.csv on the map by using basemap.

/geography/merged.py: merge genre attribute of otherdata.csv into geo_information_coordinates.csv and geo_information_nan_location_coordinates.csv. Output files are geo_information_coordinates_final.csv and geo_information_nan_location_coordinates_final.csv.

/geography/kmean_cluster.py: runs KMeans algorithm for latitudes and longitudes of geo_information_final.csv and add a cluster-id column. The output file is geo_information_final_cluster.csv.

/geography/geo_cluster_display.R: R scripts for display of geographical information. You need to install ggmap and ggplot2 packages.

## Arguments:
	Note: Path information will need to be changed. Examples provided below. 
	- msd: Path to MillionSongSubset or MillionSongDataset folders. Ex: '/bin/usr/path/to/dir/MillionSongSubset'
	- msdtoolkit: Path to MSongsDB folder. This is a toolkit that can be downloaded from the MillionSongDataset website. Ex: '/bin/usr/path/to/dir/MSongsDB' 
	- tagtraum: Path to Tagtraum dataset (msd_tagtraum_cd2.cls)
	- mxm: Path to MXM dataset (mxm_dataset.db) '/home/usr/path/to/dir/MillionSongSubset/mxm_dataset.db'

## Executing the script:
To run the extract_data.py script, you need to have python3 installed on your machine. Information on getting python3 can be found [here](https://www.python.org/downloads/). In Python 2.7 the csv file will be incorrectly generated due to unicode formatting behavior. Formatting the detailed information in the MSD in csv format is not realistic due to the sheer size of the subset. To extract that data, see [here](http://labrosa.ee.columbia.edu/millionsong/pages/basic-getters-functions).

## CSV Generator
There are two scripts that grab data attributes from the MSD, converting the data into a csv format. The python script `getData.py` takes a text file as a command line argument, which is then parsed into an array containing the desired fields.The other file, `get_info.py`, gets the fields from the user directly from the command line. This file is also written for python version 2.7.10. 

## Running the Programs:

get_info.py: `python get_info.py track_id song_id tempo`

getData.py: `python3 getData testGetData.txt`
        
extract_data.py: `python3 extract_data.py`