from django.shortcuts import render

def index (request):
   return render(request, 'app/index.html')

def home(request):
   return render(request, 'app/index.html')
