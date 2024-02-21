import os
import pandas as pd
from models import Enrollment

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