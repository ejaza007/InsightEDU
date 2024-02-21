from django.db import models

# Create your models here.

#Model for Enrollment Table
class Enrollment(models.Model):
    number_of_students = models.IntegerField()
    number_of_low_income_students = models.IntegerField()
    year = models.IntegerField()
    school_number = models.IntegerField(primary_key=True)

#Model for School Table
class School (models.Model):
    aun = models.IntegerField()
    school_name = models.CharField(max_length=255)
    school_number = models.IntegerField()

#Model for Keystone Exam
class KeystoneExam(models.Model):
    id = models.IntegerField(primary_key=True)
    school_number = models.IntegerField()
    year = models.IntegerField()
    percentage_bio_proficient = models.FloatField()
    percentage_lit_proficient = models.FloatField()
    percentage_alg_proficient = models.FloatField()

#Model for PSSA Exam
class PssaExam(models.Model):
    percentage_eng_proficient = models.FloatField()
    percentage_math_proficient = models.FloatField()
    percentage_science_proficient = models.FloatField()
    school_number = models.IntegerField(primary_key=True)
    year = models.IntegerField()

#Model for District Form
class DistrictForm (models.Model):
    county_name = models.CharField(max_length=255)
    district_id=models.IntegerField(primary_key=True)
    district_name=models.CharField(max_length=255)

#Model for County Form
class CountyForm (models.Model):
    county_id=models.IntegerField(primary_key=True)
    county_name=models.CharField(max_length=255)

class DistrictF(models.Model):
    county_n = models.CharField(max_length=255)
    d_id=models.IntegerField(primary_key=True)
    d_name=models.CharField(max_length=255)

class Category(models.Model):
    school_number = models.IntegerField(primary_key=True)
    high_school = models.IntegerField()
    middle_school = models.IntegerField()
    elementary_school = models.IntegerField()
    
class Type(models.Model):
    school_number = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=255)
    high_school = models.IntegerField()
    middle_school = models.IntegerField()
    elementary_school = models.IntegerField()
    
