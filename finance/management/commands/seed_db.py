from django.core.management.base import BaseCommand

from finance.utils.file_reader import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        seed_data_from_files('grants')
        seed_data_from_files('loans')


