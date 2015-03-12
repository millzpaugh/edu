from datetime import datetime
import os
import re

from funcy import last, first
import glob
import pandas


class FileCouldNotBeReadException(Exception):
    def __init__(self, filename=None):
        self.filename = filename

    def __str__(self):
        return 'Cannot read file {name}'.format(name=self.filename)

def seed_data_from_grant_files(funding_type):
    grant_files = _retrieve_excel_files(funding_type)
    for file in grant_files:
        grant_reader = GrantFileReader(file=file)
        grant_data = grant_reader.retrieve_grant_file_data()

def seed_data_from_loan_files(funding_type):
    grant_files = _retrieve_excel_files(funding_type)
    for file in grant_files:
        loan_reader = LoanFileReader(file=file)
        loan_data = loan_reader.retrieve_grant_file_data()

def _retrieve_excel_files(funding_type):
    return [file_path for file_path in glob("./files/" + funding_type + os.sep + "*.xls")]


class GrantFileReader():
    def __init__(self, file):
        file = self.file

    def get_grant_year(self):
        return int('20' + self.filename[-8:][:-6])

    def parse_filename_to_retrieve_grant_spreadsheet_name(self):
        return self.file[-12:][:-10] + ' ' + self.file[-10:][:-6] + ' YTD'

    def retrieve_grant_file_data(self):
        try:
            data = pandas.io.excel.read_excel(self.file, self.parse_filename_to_retrieve_grant_spreadsheet_name())
            return data
        except:
            raise FileCouldNotBeReadException()

class LoanFileReader():
    def __init__(self, file):
        file = self.file

    def get_loan_year(self):
        return int(self.file[-11:][:-7])

    def retrieve_loan_file_data(self):
        try:
            data = pandas.io.excel.read_excel(self.file, 'Award Year Summary')
            return data
        except:
            raise FileCouldNotBeReadException()







