from django.core.management.base import BaseCommand

from finance.utils.data_parser import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        seed_data_from_files('grants')


