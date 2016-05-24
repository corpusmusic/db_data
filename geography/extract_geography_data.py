#coding -*- utf-16 _*-
import os
import sys
import glob
import numpy as np
import argparse

msd_code_path='../'
assert os.path.isdir(msd_code_path),'wrong path' # sanity check
# we add some paths to python so we can import MSD code
# Ubuntu: you can change the environment variable PYTHONPATH
# in your .bashrc file so you do not have to type these lines
sys.path.append( os.path.join(msd_code_path,'PythonSrc') )

# imports specific to the MSD
import hdf5_getters as GETTERS


# we define this very useful function to iterate the files
def apply_to_all_files(basedir,func=lambda x: x,ext='.h5'):
    cnt = 0
    
    track_info = np.array(['track_id','artist_location','artist_latitude','artist_longitude'])
    nan_track_info = np.array(['track_id','artist_location','artist_latitude','artist_longitude'])
    nonnan_track_info = np.array(['track_id','artist_location','artist_latitude','artist_longitude'])

    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
            
        # count files
        cnt += len(files)
            
        # apply function to all files
        for f in files:
            track_info_row = func(f)
            track_info_row[1] = track_info_row[1].replace(',','/')

            if track_info_row[2] == 'nan' or track_info_row[3] == 'nan':
                nan_track_info = np.vstack([nan_track_info, track_info_row])
            else:
                nonnan_track_info = np.vstack([nonnan_track_info, track_info_row])
                        
            track_info = np.vstack([track_info, track_info_row])
             
    with open('geo_information.csv', 'w') as outfile:
        np.savetxt(outfile, track_info, delimiter=',', fmt="%s")

    with open('geo_information_nan.csv', 'w') as nanfile:        
        np.savetxt(nanfile, nan_track_info, delimiter=',', fmt="%s")                  
    
    with open('geo_information_coordinates.csv', 'w') as nonnanfile:
        np.savetxt(nonnanfile, nonnan_track_info, delimiter=',', fmt="%s")

    return cnt


def get_geography_information(h5file):
    h5 = GETTERS.open_h5_file_read(h5file)

    track_id = GETTERS.get_track_id(h5)
    artist_location = GETTERS.get_artist_location(h5)
    artist_latitude = GETTERS.get_artist_latitude(h5)
    artist_longitude = GETTERS.get_artist_longitude(h5)
    
    h5.close()

    return np.array([track_id, artist_location, artist_latitude, artist_longitude])
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--msdsubset", dest="msdsubset")
    args = parser.parse_args()

    if args.msdsubset:
        msd_subset_path = args.msdsubset
    else:
        msd_subset_path='../subset'
    assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

    print apply_to_all_files(msd_subset_path, get_geography_information)


if __name__ == "__main__":
    main()