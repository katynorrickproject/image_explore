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

def check_dicoms(dicom_set):
    for index,dcm in enumerate(dicom_set):
        try:
            dcm[0x00100010]
        except:
            dicom_set.pop(index)
            check_dicoms(dicom_set)
    return dicom_set

def get_train():
    train_url = 'Data/dicom-images-train'
    return check_dicoms(load_dicoms(train_url))

def get_test():
    test_url = 'Data/dicom-images-test'
    return check_dicoms(load_dicoms(test_url))
