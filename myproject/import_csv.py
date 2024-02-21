import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.py')
django.setup()

from django.db import models

# Model for Enrollment Table
class Enrollment(models.Model):
    number_of_students = models.IntegerField()
    number_of_low_income_students = models.IntegerField()
    year = models.IntegerField()
    school_number = models.IntegerField(primary_key=True)

def import_enrollment_data_from_csv():
    file_path = os.path.join(os.path.dirname(__file__), 'Enrollment.csv')
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        Enrollment.objects.create(
            number_of_students=row['number_of_students'],
            number_of_low_income_students=row['number_of_low_income_students'],
            year=row['year'],
            school_number=row['school_number']
        )

# Call the import function
import_enrollment_data_from_csv()