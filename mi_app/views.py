from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, "mi_app/main.html")

def habilidades(request):
    return render(request, "mi_app/habilidades.html")