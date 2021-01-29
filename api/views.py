from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from   rest_framework.exceptions import bad_request
from django.http import HttpResponse

import requests
import json


# Create your views here.

@api_view(['GET'])
def get_api_overview(request):
    data = [
        {
            'base_url': '/api/keyword',
            'method': 'POST',
            'data': {
                'key[]': 'list of keywords',
                'country': 'string country, ex: us',
                'api_key': 'Your API key'

            }

        }
    ]

    return Response(data)


@api_view(['POST'])
def get_keyword(request):
    base_url = "https://api.keywordseverywhere.com/v1/get_keyword_data"
    if not request.data:
        return HttpResponse(bad_request(request, exception=None))
    api_key = request.data['api_key']
    my_headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    response = requests.post(base_url, data=request.data, headers=my_headers)
    return Response(json.loads(response.content.decode('utf-8')))
