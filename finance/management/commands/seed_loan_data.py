from django.core.management.base import BaseCommand

from finance.utils.data_parser import *
from finance.management.file_retriever import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        files = retrieve_excel_files('loans')
        seed_data_from_files(files,'loans')