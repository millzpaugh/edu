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
        self.grant_file_reader = FileReader(file="finance/utils/ed_data/grants/Q41213AY.xls",
                                            funding_type="grants")
        self.loan_file_reader = FileReader(file="finance/utils/ed_data/loans/DL_Dashboard_AY2011_2012_Q4.xls",
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




