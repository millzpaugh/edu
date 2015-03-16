import pandas


class FileCouldNotBeReadException(Exception):
    def __init__(self, filename=None):
        self.filename = filename

    def __str__(self):
        return 'Cannot read file {name}'.format(name=self.filename)

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
            file = self.file
            raise FileCouldNotBeReadException('File:' + file)





