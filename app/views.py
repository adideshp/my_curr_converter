from django.shortcuts import render
import simplejson as json
from django.template import loader
from currConv.settings import BASE_CURRENCY
from requests.exceptions import HTTPError
#from currConv.settings import xecd

# Create your views here.
from django.http import HttpResponse
import requests
from .forms import CurrencyForm

#Helper functions
def get_currencies():
    # Default currency is EURO    
    req = requests.get('https://api.exchangeratesapi.io/latest')
    template = loader.get_template('app/index.html')
    curr = req.json()
    return list(curr['rates'].keys())


def update_curr_list(curr_list):
    #Add EUR as a currency in the list
    curr_list.append("EUR")
    return curr_list
 
def create_choices(curr_list):
    choices = []
    for curr in curr_list:
        choices.append((curr, curr))
    return tuple(choices)

# Create your views here.
def index(request):
    template = loader.get_template('app/index.html')
    curr_list = update_curr_list(get_currencies())
    form = CurrencyForm(create_choices(curr_list))
    context = {
        'currencies': curr_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))


def convert(request):
    curr_list = update_curr_list(get_currencies())
    choices = create_choices(curr_list)
    form = CurrencyForm(choices, request.GET)
    errors = []
    if form.is_valid():
        data = form.cleaned_data
        api = 'https://api.exchangeratesapi.io/latest'
        params = {
            "base": data["from_curr"],
            "symbols": data["to_curr"]
        }  
    
        try:
            res = requests.get(url=api, params=params)
            if res.status_code == requests.codes.ok:
                res = res.json()
                result = res["rates"][data["to_curr"]] * float(data["amount"])
            else:
                errors.append("Status code:" + str(res.status_code))
                
        except HTTPError as http_err:
            errors.append("HTTP Error occoured. Please try again")    
    
    template = loader.get_template('app/index.html')
    
    form = CurrencyForm(choices)

    context = {
        'to': data["to_curr"],
        'from': data["from_curr"],
        'org_amount': data["amount"],
        'result': result,
        'form': form,
        'errors': errors
    }

    return HttpResponse(template.render(context, request))


