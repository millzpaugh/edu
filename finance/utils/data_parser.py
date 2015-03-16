from finance.models import School, Loan, Grant, LOAN_TYPE_CHOICES, GRANT_TYPE_CHOICES
from finance.utils.file_reader import FileReader
from os.path import  dirname, realpath
import os
import glob

class RowCouldNotBeSaved(Exception):
    pass

def seed_data_from_files(files, funding_type):
    for file in files:
        file_reader = FileReader(file=file,funding_type=funding_type)
        data = file_reader.retrieve_file_data()
        year = file_reader.get_year()

        if funding_type == 'grants':
            save_grant_data_from_single_file(data, file, year)
        if funding_type == 'loans':
            save_loan_data_from_single_file(data, file, year)

def save_loan_data_from_single_file(data, file, year):
    for row in data:
        school = _get_or_create_school(row)
        save_loans_from_single_row(row,school,file, year)
    return True

def save_grant_data_from_single_file(data, file, year):
    for row in data:
        school = _get_or_create_school(row)

        try:
            #figure out how to extract grant type as kv pair
            #add additional programs from 2006 - 2010
            column_loan_types = [5,7,9]

            for column in column_loan_types:
                if row[column] is not 0:
                    grant_data = extract_row_data_for_specific_grant_type_at_single_school(row, column, column_loan_types)

                    grant, created = Grant.objects.get_or_create(school_id=school,grant_type=grant_data['grant_type'],
                                                                recipients=grant_data['recipients'],
                                                                grant_money_disbursed=grant_data['grant_money_disbursed'],
                                                                year=year)
                    if created:
                        grant.save()
                    else:
                        continue

        except RowCouldNotBeSaved:
            error = 'Error! Grant with School ID: ' + str(school.name) + ' in File ' + file + ' cannot be saved.'
            raise RowCouldNotBeSaved(error)

def save_loans_from_single_row(row, school, file, year):
    try:
        column_loan_types = [5,10,15,20,25]
        for column in column_loan_types:
            if row[column] is not 0:
                loan_data = extract_row_data_for_specific_loan_type_at_single_school(row,column, column_loan_types)

                loan, created = Loan.objects.get_or_create(school_id=school,
                                               loan_type=loan_data['loan_type'],
                                               recipients=loan_data['recipients'],
                                               number_of_loans=loan_data['number_of_loans'],
                                               loan_money_originated=loan_data['loan_money_originated'],
                                               number_of_disbursements=loan_data['number_of_disbursements'],
                                               loan_money_disbursed=loan_data['loan_money_disbursed'],
                                               year=year)
                if created:
                    loan.save()
                else:
                    continue

    except:
        error = 'Error! Loan with School ID: ' + str(school.name) + ' in File ' + file + ' cannot be saved.'
        raise RowCouldNotBeSaved(error)

def extract_row_data_for_specific_loan_type_at_single_school(row,column,column_loan_types):
    index = column_loan_types.index(column)

    if row[column] is not 0:
        return {'recipients':row[column],
                'loan_type':LOAN_TYPE_CHOICES[index][0],
                'number_of_loans':row[column + 1],
                'loan_money_originated':row[column + 2],
                'number_of_disbursements':row[column + 3],
                'loan_money_disbursed':row[column + 4]}
    else:
        return {}

def extract_row_data_for_specific_grant_type_at_single_school(row,column, column_loan_types):
    index = column_loan_types.index(column)

    if row[column] is not 0:
        return {'recipients':row[column],
                'grant_type':GRANT_TYPE_CHOICES[index][0],
                'grant_money_disbursed':row[column + 1]}
    else:
        return {}

def _get_or_create_school(row):
    school = School.objects.filter(name=row[1].strip()).first()

    if school:
        school = school
    else:
        school = School.objects.create(name=row[1].strip(),state=row[2].strip(),
                                                  zip=row[3], sector=row[4].lower())
        school.save()

    return school
