#!/usr/bin/env python

import h5py
import hdf5_getters as getter
import argparse
import os
import numpy as np

def getInfo(files):
    infoList = np.array(['tid', 'artist', 'song'])
    
    for fil in files:
        curFile = getter.open_h5_file_read(fil)
        tid = fil.split('/')[-1].split('.')[0]
        curArtist = getter.get_artist_name(curFile)
        curTitle = getter.get_title(curFile)
        curArr = np.array([tid, curArtist, curTitle])
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
        dirName = '/home/paul/gits/db_data/subset/'
    
    files = [dirName + fil for fil in os.listdir(dirName) if fil.endswith('.h5')]
    infos = getInfo(files)
    
    with open('trackInfo.tsv', 'w') as f:
        np.savetxt(f, infos, delimiter='\t', fmt="%s")
    print 'trackInfo.tsv created'

if __name__=='__main__':
    main()
