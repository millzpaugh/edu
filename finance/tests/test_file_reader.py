# from funcy import first, second, last
# from mock import patch, call
# import pytest
# from datetime import datetime
# import pytest
from django.test import TestCase

from finance.utils.file_reader import *
from finance.utils.data_parser import *
from finance.models import School, Loan, Grant


class TestFileReader(TestCase):
    def setUp(self):
        self.grant_file_reader = FileReader(file="finance/utils/files/grants/Q41213AY.xls",
                                            funding_type="grants")
        self.loan_file_reader = FileReader(file="finance/utils/files/loans/DL_Dashboard_AY2011_2012_Q4.xls",
                                           funding_type="loans")

    def test_get_year(self):
        self.assertEqual(self.grant_file_reader.get_year(), 2013)
        self.assertEqual(self.loan_file_reader.get_year(), 2012)

    def test_retrieve_file_data(self):
        grant_data = self.grant_file_reader.retrieve_file_data()
        loan_data = self.loan_file_reader.retrieve_file_data()
        self.assertEqual(list(loan_data[0]), [u'00106100', u'ALASKA PACIFIC UNIVERSITY', u'AK', u'995084672', u'PRIVATE',
                                        235, 254, 1022825, 403, 951601, 115, 127, 859589, 203, 827795, 254, 270,
                                        1293141, 437, 1188068, 106, 120, 1258719, 188, 1147761, 43, 49, 710516, 81,
                                        690761, 7, 10, 70663, 15, 70647])
        self.assertEqual(list(grant_data[0]), [100200, u'ALABAMA AGRICULTURAL & MECHANICAL UNIVERSITY                          ',
                                                u'AL', 357621357, u'PUBLIC', 79, 131016.52, 6, 6500, 0, 0])


class TestLoanDataRetrieval(TestCase):
    def setUp(self):
        self.year = 2012
        self.file = "finance/utils/files/loans/DL_Dashboard_AY2011_2012_Q4.xls"
        self.school = School.objects.create(name='ALASKA PACIFIC UNIVERSITY',state='AK',zip='995084672', sector='Private')
        self.row = ['00106100', 'ALASKA PACIFIC UNIVERSITY', 'AK', '995084672', 'PRIVATE',
                    235, 254, 1022825, 403, 951601, 115, 127, 859589, 203, 827795, 254, 270,
                    1293141, 437, 1188068, 106, 120, 1258719, 188, 1147761, 43, 49, 710516, 81,
                    690761, 7, 10, 70663, 15, 70647]
        self.column = 5
        self.column_types = [5,10,15,20,25,30]


    def test_extract_row_from_data(self):
        loan = extract_row_data_for_specific_loan_type_at_single_school(self.row,self.column, self.column_types)

        self.assertEqual(loan['recipients'], 235)
        self.assertEqual(loan['loan_money_originated'], 1022825)
        self.assertEqual(loan['loan_money_disbursed'], 951601)

class TestGrantDataRetrieval(TestCase):
    def setUp(self):
        self.row = [100200, 'ALABAMA AGRICULTURAL & MECHANICAL UNIVERSITY','AL', 357621357, u'PUBLIC', 79, 131016.52, 6, 6500, 0, 0]
        self.column = 5
        self.column_types = [5,7,9]


    def test_extract_row_from_data(self):
        grant = extract_row_data_for_specific_grant_type_at_single_school(self.row,self.column, self.column_types)

        self.assertEqual(grant['recipients'], 79)
        self.assertEqual(grant['grant_type'], 'pell')
        self.assertEqual(grant['grant_money_disbursed'], 131016.52)



