from django.core.management.base import BaseCommand
import csv
from base.models import QuizQuestion, Factor, Job, MultiFactorQuestion
import os

# super user => username = ayush, password = AYUSH001
# username = a, email = a@gmail.com, password = abc


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Get the project's base directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        try:
            csv_data_dir = os.path.join(base_dir, 'csvdata')
            self.load_quiz_questions(os.path.join(
                csv_data_dir, 'singlefactor_que.csv'))
            self.load_multi_factor_questions(os.path.join(
                csv_data_dir, 'multifactor_que.csv'))
            self.load_factors()
            self.load_jobs(os.path.join(csv_data_dir, 'Jobs_Artistic.csv'))
            self.load_jobs(os.path.join(csv_data_dir, 'Jobs_Conventional.csv'))
            self.load_jobs(os.path.join(csv_data_dir, 'Jobs_Enterprising.csv'))
            self.load_jobs(os.path.join(
                csv_data_dir, 'Jobs_Investigative.csv'))
            self.load_jobs(os.path.join(csv_data_dir, 'Jobs_Realistic.csv'))
            self.load_jobs(os.path.join(csv_data_dir, 'Jobs_Social.csv'))
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))

    def load_quiz_questions(self, csv_file_name):
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                QuizQuestion.objects.create(
                    Q_id=row['Q_id'],
                    Question=row['Question'],
                    primaryfact=row['primaryfact'],
                    otherfact=row['otherfact']
                )

    def load_multi_factor_questions(self, csv_file_name):
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                MultiFactorQuestion.objects.create(
                    Q_id=row['Q_id'],
                    Question=row['Question'],
                    primaryfacts=row['primaryfacts'],
                    otherfacts=row['otherfacts']
                )

    def load_factors(self):
        factors_data = [
            {'code': 'a', 'name': 'Artistic'},
            {'code': 'c', 'name': 'Conventional'},
            {'code': 'e', 'name': 'Enterprising'},
            {'code': 'i', 'name': 'Investigative'},
            {'code': 'r', 'name': 'Realistic'},
            {'code': 's', 'name': 'Social'}
        ]
        for factor_info in factors_data:
            Factor.objects.create(**factor_info)

    def load_jobs(self, csv_file_name):
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                Job.objects.create(
                    interest_code=row['Interest Code'],
                    occupation=row['Occupation']
                )
