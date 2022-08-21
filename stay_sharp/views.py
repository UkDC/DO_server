from django.shortcuts import render

# Create your views here.

def account_table(request):
    return render(request, 'Account-table.html')

def calculation(request):
    return render(request, 'Calculation.html')

def main(request):
    return render(request, 'Main.html')

def login(request):
    return render(request, 'Login.html')

def drawing(request):
    return render(request, 'Drawing.html')