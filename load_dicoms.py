''' To load dicom training data use get_train()
To load dicom test data use get_test() '''

import os
import pydicom



def load_dicoms(path):
    ## Adds a '/' to the end of the file path if it isn't already there
    if path[-1] != '/':
        path += '/'
    x = []
    for dir_ in os.listdir(path):
        new_path = path+dir_
        for subdir_ in os.listdir(new_path):
            for file in os.listdir(new_path+'/'+subdir_):
                x.append(pydicom.dcmread(new_path+'/'+subdir_+'/'+file,force=True))

    return x

def get_train():
    train_url = 'Data/dicom-images-train'
    return load_dicoms(train_url)

def get_test():
    test_url = 'Data/dicom-images-test'
    return load_dicoms(test_url)
