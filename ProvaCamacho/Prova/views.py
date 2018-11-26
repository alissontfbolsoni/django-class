from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request: HttpResponse):
    return render(request, 'index.html')

# def client_list(request: HttpRequest):
#     clients = Client.objects.all()
#     context = {'clients': clients}
#     return render(request, 'client.html', context)
