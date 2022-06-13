from django.shortcuts import render

# Create your views here.
def plantilla(request):
    return render(request, 'plantilla.html', {})