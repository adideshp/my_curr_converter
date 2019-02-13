from django.shortcuts import render
import simplejson as json
from django.template import loader
from currConv.settings import currencies
from currConv.settings import xecd

# Create your views here.
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    template = loader.get_template('app/index.html')
    context = {
        'currencies': currencies
    }
    return HttpResponse(template.render(context, request))


def convert(request):
    to_curr = request.GET['to']
    from_curr = request.GET['from']
    amount = request.GET['amount']
    res = xecd.convert_from(from_curr, to_curr, amount)
    template = loader.get_template('app/index.html')
    context = {
        'currencies': currencies,
        'to': to_curr,
        'from': from_curr,
        'org_amount': amount,
        'result': res["to"][0]["mid"]
    }
    return HttpResponse(template.render(context, request))