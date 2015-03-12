from datetime import datetime
import os
from os.path import  dirname, realpath
import re
from funcy import last, first
import glob
import pandas
from finance.models import School, Loan, Grant


class FileCouldNotBeReadException(Exception):
    def __init__(self, filename=None):
        self.filename = filename

    def __str__(self):
        return 'Cannot read file {name}'.format(name=self.filename)

class RowCouldNotBeSaved(Exception):
    pass


def seed_data_from_files(funding_type):
    files = _retrieve_excel_files(funding_type)
    for file in files:
        file_reader = FileReader(file=file,funding_type=funding_type)
        data = file_reader.retrieve_file_data()
        if funding_type == 'grants':
            year = file_reader.get_year()
            save_grant_data_from_single_file(data, file, year)
        if funding_type == 'loans':
            save_loan_data_from_single_file(data, file)

def _retrieve_excel_files(funding_type):
    current_dir = dirname(realpath(__file__))
    return [file for file in glob.glob(current_dir + "/files/" + funding_type + os.sep + "*.xls")]

def save_loan_data_from_single_file(data):
    for row in data:
        pass

def save_grant_data_from_single_file(data, file, year):
    for row in data:
        dpt_of_ed_id = row[0]
        try:
            school, exists = School.objects.get_or_create(name=row[1],state=row[2],
                                                  zip=row[3], sector=row[4].lower())
            if exists:
                school = school
            else:
                school.save()

            #figure out how to extract grant type as kv pair
            #add additional programs from 2006 - 2010
                if row[5] is not 0:
                    pell_grant, exists = Grant.objects.get_or_create(school_id=school,grant_type='pell',
                                                                    recipients=row[5],grant_money_disbursed=row[6],year=year)
                    if not exists:
                        pell_grant.save()

                if row[7] is not 0:
                    teach_grant, exists = Grant.objects.get_or_create(school_id=school,grant_type='teach',
                                                                recipients=row[7],grant_money_disbursed=row[8], year=year)
                    if not exists:
                        teach_grant.save()

                if row[9] is not 0:
                    iraq_grant, exists = Grant.objects.get_or_create(school_id=school,grant_type='iraq_afghan',
                                                    recipients=row[7],grant_money_disbursed=row[8], year=year)
                    if not exists:
                        iraq_grant.save()
        except:
            error = 'Error! School ID: ' + str(dpt_of_ed_id) + ' in File ' + file + ' cannot be saved.'
            raise RowCouldNotBeSaved(error)

class FileReader():
    def __init__(self, file, funding_type):
        self.file = file
        self.funding_type = funding_type

    def get_year(self):
        if self.funding_type == 'loans':
            return int(self.file[-11:][:-7])
        if self.funding_type == 'grants':
            return int('20' + self.file[-8:][:-6])

    def retrieve_file_data(self):
        try:
            data = pandas.io.excel.read_excel(self.file, 1)
            return data.values[5:]
        except:
            raise FileCouldNotBeReadException()










