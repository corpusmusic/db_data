#coding -*- utf-16 _*-
import os
import sys
import time
import glob
import codecs
import datetime
import argparse
import sqlite3
import numpy as np # get it at: http://numpy.scipy.org/
from csv import DictWriter
from shutil import copyfile

# imports specific to the MSD


# we define this very useful function to iterate the files
def apply_to_all_files(basedir,func=lambda x: x,ext='.h5'):
    cnt = 0
    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        # count files
        cnt += len(files)
        # apply function to all files
        for f in files :
            func(f)       
    return cnt


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--msd", dest="msd")
    parser.add_argument("--msdtoolkit", dest="msdt")
    parser.add_argument("--tagtraum", dest="tagtraum")
    parser.add_argument("--mxm", dest="mxm")
    parser.add_argument("--cs", dest="commonsongs")
    args = parser.parse_args()


    if args.msd:
        msd_subset_path = args.msd
    else:
        msd_subset_path='/home/rcrimi/corpusMusic/MillionSongSubset'
    msd_subset_data_path=os.path.join(msd_subset_path,'data')
    msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
    assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

    if args.msdt:
        msd_code_path = args.msdt
    else:
        msd_code_path='/home/rcrimi/Documents/MSongsDB'
    assert os.path.isdir(msd_code_path),'wrong path' # sanity check
    sys.path.append( os.path.join(msd_code_path,'PythonSrc'))

    if args.tagtraum:
        tagtraum_path = args.tagtraum
    else:
        tagtraum_path = "msd_tagtraum_cd2.cls"
    assert os.path.isfile(tagtraum_path)

    if args.mxm:
        mxm_path = args.mxm
    else:
        mxm_path = '/home/rcrimi/corpusMusic/MillionSongSubset/mxm_dataset.db'
    assert os.path.isfile(mxm_path)

    if args.commonsongs:
        commonsongs_path = args.commonsongs
    else:
        commonsongs_path = "common_songs.txt"

    import hdf5_getters as GETTERS

    full_data = [["track_id", "genre", "lyrics"]]

    tagtraum_dict = {}
    with open(tagtraum_path) as t:
        tagtraum_data = t.readlines()
        for line in tagtraum_data:
            d = line.split("\t")
            tagtraum_dict[d[0]] = d[1:]



    with open(commonsongs_path) as f:
        data = f.readlines()
        for track_id in data:
            track_id = track_id.rstrip("\n")
            filename = '/home/rcrimi/corpusMusic/MillionSongSubset/data/'
            filename += "/".join(list(track_id[2:5]))+"/"
            filename += track_id + ".h5"
            if os.path.isfile(filename):
                #copyfile(filename, "/home/rcrimi/corpusMusic/MillionSongSubset/subset/%s"%(track_id+".h5"))

                l = [track_id]
                genres =  tagtraum_dict[track_id.rstrip("\n")]
                l.append("|".join([g.rstrip("\n") for g in genres]))

                conn = sqlite3.connect(mxm_path)
                q = "SELECT * FROM lyrics WHERE track_id == '%s'" % track_id
                res = conn.execute(q)
                response = res.fetchall()
                conn.close()
                lyrics = ""
                for word in response:
                    lyrics += word[2]+"|"
                    lyrics += str(word[3])+" "
                l.append(lyrics)

                full_data.append(l)
    
    tmplist = np.array(full_data)
    #outfile = codecs.open("otherdata.csv", mode="wb", encoding="utf-8")
    with open('otherdata.csv', "w") as outfile:
        for line in full_data:
            outfile.write(str(line).lstrip("[").rstrip("]"))
        #np.savetxt(outfile, tmplist, delimiter=",", fmt="%s")
    '''
    trackids = []
    for track in data:
        track_id = track.split("\t")[0]
        trackids.append(track_id)

    conn = sqlite3.connect(os.path.join(msd_subset_path, mxm_path))
    # we build the SQL query
    q = "SELECT DISTINCT track_id FROM lyrics WHERE track_id IN %s" % str(trackids).replace("[", "(").replace("]", ")")
    # we query the database
    t1 = time.time()
    res = conn.execute(q)
    all_artist_names_sqlite = res.fetchall()
    t2 = time.time()
    print 'all artist names extracted (SQLite) in:',strtimedelta(t1,t2)
    # we close the connection to the database
    conn.close()
    # let's see some of the content
    for k in range(len(all_artist_names_sqlite)):
        print all_artist_names_sqlite[k][0]
    '''


if __name__ == "__main__":
    main()
