from django.shortcuts import get_object_or_404#, render
from django.http import HttpResponse
from pricing.models import Country
# PanelProvider, Country, Location, LocationGroup, TargetGroup

# The authentication type is up to you and you should assume there is
# no firewall so the server would be public facing and needs to be secured properly when necessary.

# first 3 private
def request_1(request, country_code):
  country = get_object_or_404(Country, country_code=country_code) #  get_list_or_404()

  return HttpResponse("Hi there! You are at %s" % country.country_code)

def request_2(request, country_code):
  return HttpResponse("Hi there! You are at request_2.")

# POST evaluate_target
def request_3(request):
  country = get_object_or_404(Country, country_code=request.POST["country_code"])

  return HttpResponseRedirect(reverse("request_2", args=(country.country_code,)))

def request_4(request, country_code):
  return HttpResponse("Hi there! You are at request_4.")

def request_5(request, country_code):
  return HttpResponse("Hi there! You are at request_5.")
