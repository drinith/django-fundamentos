from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    html = "<html>teste</html>"
    return render(request,"contas/home.html") 