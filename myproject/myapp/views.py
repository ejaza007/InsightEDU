from django.shortcuts import render
from .models import Enrollment
from .models import School
from .models import PssaExam
from .models import KeystoneExam
from .models import DistrictF
from django.http import JsonResponse
from .models import Category
from .models import Type


#from .models import District  

def profile_view(request):
    #districts = District.objects.all()  # Query all district records from the database
    data = Enrollment.objects.all() #Fetch all the records from the Table
    data1 = School.objects.all()
    year = request.GET.get('year', None)
    #Filter the records based on the year
    if year:
        data = Enrollment.objects.filter(year=year) #Filter records based on the year
    else:
        data = Enrollment.objects.all() #Fetch all the records if nothing has been selected
    #print(districts)  
    return render(request, 'myapp/profile.html', {'data': data, 'data1':data1})  # Pass the district data to the template

def index_view(request):
    data = Enrollment.objects.all()  # Fetch all records from Enrollment
    return render(request, 'myapp/index.html', {'data': data})

def get_counties(request):
    counties = DistrictF.objects.values_list('county_n', flat=True).distinct()
    return JsonResponse(list(counties), safe=False)

def get_districts(request, county_name):
    districts = DistrictF.objects.filter(county_n=county_name).values_list('d_name', flat=True)
    return JsonResponse(list(districts), safe=False)

def view_data(request):
    data = Enrollment.objects.all()  # Fetch all records from Enrollment
    return render(request, 'myapp/view.html', {'data': data})

def compare_view(request):
    data5 = DistrictF.objects.all()
    print(data5)
    return render(request, 'myapp/compare.html', {'data5':data5})

def display_table1_data(request):
    data1 = School.objects.all()
    print(data1)
    return render(request, 'myapp/data.html', {'data1': data1})

def display_pssa_exam_data(request):
    data2 = PssaExam.objects.all()
    print(data2)
    return render(request, 'myapp/examp.html', {'data2': data2})

def display_keystone_exam_data(request):
    data3 = KeystoneExam.objects.all()
    print(data3)
    return render(request, 'myapp/keystone.html', {'data3': data3})

def display_district_data(request):
    data4 = DistrictForm.objects.all()
    print(data4)  # Check if data is correctly fetched
    return render(request, 'myapp/district.html', {'data4': data4})

def compare_data(request):
    data5 = DistrictF.objects.all()
    return render(request, 'myapp/compare.html', {'data5':data5})

def get_school_names(request, school_type):
    schools = School.objects.filter(type=school_type).values('school_number', 'school_name')
    return JsonResponse(list(schools), safe=False)

def get_school_ids(request, school_type):
    if school_type == 'elementary':
        schools = Category.objects.filter(elementary_school=1)
    elif school_type == 'middle':
        schools = Category.objects.filter(middle_school=1)
    elif school_type == 'high':
        schools = Category.objects.filter(high_school=1)
        print ("schools",schools.count())
    else:
        return JsonResponse({'error': 'Invalid school type'}, status=400)

    school_ids = [school.school_number for school in schools]
    print("Fetched schools:", school_ids)
    response_data = {'school_ids': school_ids}
    print("Sending response:", response_data)
    return JsonResponse(response_data)

def get_school_names_by_type(request, school_type):
    if school_type == 'elementary':
        schools = Type.objects.filter(elementary_school=1)
    elif school_type == 'middle':
        schools = Type.objects.filter(middle_school=1)
    elif school_type == 'high':
        schools = Type.objects.filter(high_school=1)
    else:
        return JsonResponse({'error': 'Invalid school type'}, status=400)

    school_data = schools.values('school_number', 'school_name')
    return JsonResponse(list(school_data), safe=False)


def get_school_yearly_data(request, school_number):
    print(KeystoneExam.objects.all())  # Check if there's data in KeystoneExam
    print(Enrollment.objects.all())    # Check if there's data in Enrollment
    data = []
    keystone_exams = KeystoneExam.objects.filter(school_number=school_number)
    
    for exam in keystone_exams:
        year = exam.year
        try:
            enrollment = Enrollment.objects.get(school_number=school_number, year=year)
            number_of_students = enrollment.number_of_students
        except Enrollment.DoesNotExist:
            number_of_students = None
        
        data.append({
            'year': year,
            'number_of_students': number_of_students,
            'percentage_bio_proficient': exam.percentage_bio_proficient,
            'percentage_alg_proficient': exam.percentage_alg_proficient,
            'percentage_lit_proficient': exam.percentage_lit_proficient,
        })

    return JsonResponse(data, safe=False)

def school_data_endpoint(request, school_number):
    data = {'sizes': [], 'successRates': [], 'lowIncomeProportion' : [] }

    keystone_exams = KeystoneExam.objects.filter(school_number=school_number)
    pssa_exams = PssaExam.objects.filter(school_number = school_number)
    
    print(f"Number of exams found: {keystone_exams.count()}")  # Debugging

    for exam in keystone_exams:
        print(f"Processing Keystone Exam for year: {exam.year}")  # Debugging
        try:
            enrollment = Enrollment.objects.get(school_number=school_number, year=exam.year)
            print(f"Found Enrollment: {enrollment.number_of_students} students")  # Debugging
            data['sizes'].append(enrollment.number_of_students)
            data['successRates'].append(((exam.percentage_alg_proficient)+(exam.percentage_bio_proficient)+(exam.percentage_lit_proficient))/3)
            data['lowIncomeProportion'].append((enrollment.number_of_low_income_students) / (enrollment.number_of_students))
        except Enrollment.DoesNotExist:
            print(f"No Enrollment found for year: {exam.year}")  # Debugging
            continue
    
    for exam_1 in pssa_exams:
        try:
            enrollment = Enrollment.objects.get(school_number=school_number, year=exam_1.year)
            print(f"Found Enrollment: {enrollment.number_of_students} students")  # Debugging
            data['sizes'].append(enrollment.number_of_students)
            data['successRates'].append(((exam_1.percentage_eng_proficient)+(exam_1.percentage_math_proficient)+(exam_1.percentage_science_proficient))/3)
            data['lowIncomeProportion'].append((enrollment.number_of_low_income_students) / (enrollment.number_of_students))
        except Enrollment.DoesNotExist:
            print(f"No Enrollment found for year: {exam.year}")  # Debugging
            continue
        

    print("Final Data:", data)  # Debugging
    return JsonResponse(data)