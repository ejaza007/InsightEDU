import os
import django
import pandas as pd

# Correctly set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

# Import the Enrollment model from the correct app
from myapp.models import Enrollment  # Replace 'myapp' with your actual app name

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
