from django.shortcuts import render

# Create your views here.
def view_fairs(request):
    return render(request, 'fairs.html')