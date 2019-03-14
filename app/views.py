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


def convert_currency_service(api, params, data):
    errors = []
    try:
        res = requests.get(url=api, params=params)
        if res.status_code == requests.codes.ok:
            res = res.json()
            result = res["rates"][data["to_curr"]] * float(data["amount"])
        else:
            errors.append("Status code:" + str(res.status_code))
            
    except HTTPError as http_err:
        errors.append("HTTP Error occoured. Please try again") 
    
    return result, errors



# Create your views here.
def index(request):
    template = loader.get_template('app/index.html')
    curr_list = update_curr_list(get_currencies())
    form = CurrencyForm(create_choices(curr_list))
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def convert(request):
    curr_list = update_curr_list(get_currencies())
    choices = create_choices(curr_list)
    form = CurrencyForm(choices, request.GET)
    initialized_form = CurrencyForm(choices, {'amount': 1, 'to_curr': "INR", 'from_curr': "EUR"})
    context = {}
    if form.is_valid():
        data = form.cleaned_data
        api = 'https://api.exchangeratesapi.io/latest'
        params = {
            "base": data["from_curr"],
            "symbols": data["to_curr"]
        }  
    
        result, errors = convert_currency_service(api, params, data)
        
        context['to'] = data["to_curr"]
        context['from'] = data["from_curr"]
        context['org_amount'] = data["amount"]
        context['result'] = result
        context['errors'] = errors    
    
    else:
        context['errors'] = ["Invalid data. Please enter correct data"]
    
    template = loader.get_template('app/index.html')
    context['form'] = initialized_form

    return HttpResponse(template.render(context, request))


