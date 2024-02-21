from django.shortcuts import render

def profile_view(request):
    return render(request, 'myapp/profile.html')

def index_view(request):
    return render(request, 'myapp/index.html')

def compare_view(request):
    return render(request, 'myapp/compare.html')
