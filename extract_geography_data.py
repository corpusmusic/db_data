#coding -*- utf-16 _*-
import os
import sys
import glob
import numpy as np
import argparse

msd_code_path='.'
assert os.path.isdir(msd_code_path),'wrong path' # sanity check
# we add some paths to python so we can import MSD code
# Ubuntu: you can change the environment variable PYTHONPATH
# in your .bashrc file so you do not have to type these lines
sys.path.append( os.path.join(msd_code_path,'PythonSrc') )

# imports specific to the MSD
import hdf5_getters as GETTERS


track_id = ''
artist_location = ''
artist_latitude = 0
artist_longitude = 0

# we define this very useful function to iterate the files
def apply_to_all_files(basedir,func=lambda x: x,ext='.h5'):
    cnt = 0
    track_geography = "track_id,artist_location,artist_latitude,artist_longitude\n"
    
    with open('geo-information.csv', "w") as outfile:
        outfile.write(track_geography)

        # iterate over all files in all subdirectories
        for root, dirs, files in os.walk(basedir):
            files = glob.glob(os.path.join(root,'*'+ext))
            
            # count files
            cnt += len(files)
            
            # apply function to all files
            for f in files :
                track_geography = ''

                func(f)

                track_geography = track_id +','+ artist_location.replace(',','/') +','+ str(artist_latitude) +','+ str(artist_longitude) +'\n'
                outfile.write(track_geography)

    outfile.close()

    return cnt


def get_geography_information(h5file):
    global track_id
    global artist_latitude
    global artist_longitude
    global artist_location

    h5 = GETTERS.open_h5_file_read(h5file)
    songidx = 0
    onegetter = ''

    numSongs = GETTERS.get_num_songs(h5)
    if songidx >= numSongs:
        print 'ERROR: file contains only',numSongs
        h5.close()
        sys.exit(0)

    # get all getters
    getters = filter(lambda x: x[:4] == 'get_', GETTERS.__dict__.keys())
    getters.remove("get_num_songs") # special case
    if onegetter == 'num_songs' or onegetter == 'get_num_songs':
        getters = []
    elif onegetter != '':
        if onegetter[:4] != 'get_':
            onegetter = 'get_' + onegetter
        try:
            getters.index(onegetter)
        except ValueError:
            print 'ERROR: getter requested:',onegetter,'does not exist.'
            h5.close()
            sys.exit(0)
        getters = [onegetter]
    getters = np.sort(getters)

    # print them
    for getter in getters:
        try:
            res = GETTERS.__getattribute__(getter)(h5,songidx)
        except AttributeError, e:
            continue
        #except AttributeError, e:
        #    if summary:
        #        continue
        #    else:
        #        print e
        #        print 'forgot -summary flag? specified wrong getter?'
        if getter[4:] == 'track_id':
            if res.__class__.__name__ == 'ndarray':
                track_id = res.shape
                #print getter[4:]+": shape =",res.shape
            else:
                track_id = res
                #print getter[4:]+":",res
        
        if getter[4:] == 'artist_location':
            if res.__class__.__name__ == 'ndarray':
                artist_location = res.shape
                #print getter[4:]+": shape =",res.shape
            else:
                artist_location = res
                #print getter[4:]+":",res

        if getter[4:] == 'artist_latitude':
            if res.__class__.__name__ == 'ndarray':
                artist_latitude = res.shape
                #print getter[4:]+": shape =",res.shape
            else:
                artist_latitude = res
                #print getter[4:]+":",res

        if getter[4:] == 'artist_longitude':
            if res.__class__.__name__ == 'ndarray':
                artist_longitude = res.shape
                #print getter[4:]+": shape =",res.shape
            else:
                artist_longitude = res
                #print getter[4:]+":",res

    h5.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--msdsubset", dest="msdsubset")
    args = parser.parse_args()

    if args.msdsubset:
        msd_subset_path = args.msdsubset
    else:
        msd_subset_path='./subset'
    assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

    print apply_to_all_files(msd_subset_path, get_geography_information)


if __name__ == "__main__":
    main()