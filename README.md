# db_data

## Description of Data

This corpus contains the overlapping data from the Million Song Dataset (MSD), MXM, and Tagtraum datasets.

otherdata.csv: Information from Tagtraum and MXM.
subset/: Information from MSD
common_songs.txt: Overlap between MXM and Tagtraum datasets
msd_tagtraum_cd2.cls: Tagtraum data


## Scripts
extract_data.py: Python script that extracts the overlapping data between MSD, MXM, and Tagtraum datasets.

### Arguments:

	- msd: Path to MillionSongSubset or MillionSongDataset folders.
	- msdtoolkit: Path to MSongsDB folder. This is a toolkit that can be downloaded from the MillionSongDataset website.
	- tagtraum: Path to Tagtraum dataset (msd_tagtraum_cd2.cls)
	- mxm: Path to MXM dataset (mxm_dataset.db)
