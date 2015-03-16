from os.path import dirname, realpath
import os
import glob

def retrieve_excel_files(funding_type):
    current_dir = os.path.dirname(realpath(__file__))
    return [file for file in glob.glob(current_dir + "/ed_data/" + funding_type + os.sep + "*.xls")]