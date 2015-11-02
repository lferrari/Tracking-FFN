from django.shortcuts import render
from django.http import HttpResponse

from ffnetworks.resolvers import resolver



def call_resolver(request):

	resolver()

	return HttpResponse("OK")



