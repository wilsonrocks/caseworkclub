from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Sup, this is the caseworkclub index")

def caseview(request,membership_number):
    return HttpResponse("This will be the view that we use, with all the notes from case {}.".format(membership_number))
