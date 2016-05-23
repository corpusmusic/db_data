#!/usr/bin/env python

import h5py
import hdf5_getters as getter
import argparse
import os
import numpy as np
lst = ['analysis_sample_rate', 'audio_md5', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'start_of_fade_out', 'tempo', 'time_signature', 'time_signature_confidence', 'track_id', 'segments_start', 'segments_confidence', 'segments_pitches', 'segments_timbre', 'segments_loudness_max', 'segments_loudness_max_time', 'segments_loudness_start', 'sections_start', 'sections_confidence', 'beats_start', 'beats_confidence', 'bars_start', 'bars_confidence', 'tatums_start', 'tatums_confidence', 'artist_mbtags', 'artist_mbtags_count', 'year']
def getInfo(files):
    d = []
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
        c = contents.split()
    f.close()    
    infoList = np.array(c) 
    for fil in files:
        curFile = getter.open_h5_file_read(fil)
        tid = fil.split('/')[-1].split('.')[0]
        for i in c:
            if c[i] in lst:

                d.append('getter.get_' + c[i] + '(curFile)')
            else:
                print('error:incorrect field')
        # curArtist = getter.get_artist_name(curFile)
        # curTitle = getter.get_title(curFile)
        curArr = np.array(d)
        infoList = np.vstack([infoList, curArr])
        curFile.close()

    return infoList

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', dest='dirName')
    args = parser.parse_args()
    if args.dirName:
        dirName = args.dirName
    else:
        dirName = '/Users/JU/Downloads/cproject/db_data/subset'
    
    files = [dirName + fil for fil in os.listdir(dirName) if fil.endswith('.h5')]
    infos = getInfo(files)
    
    with open('trackInfo.tsv', 'w') as f:
        np.savetxt(f, infos, delimiter='\t', fmt="%s")
    print ('trackInfo.tsv created')

if __name__=='__main__':
    main()