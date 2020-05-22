from django.shortcuts import render

import sys

# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


import pandas as pd

# Create your views here.
def keyboard(request):

    return JsonResponse({
        'type': 'text',
	'test': sys.path
    })

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    return_str = str(return_str).strip()

    if return_str == 'test':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': 'test 성공입니다.'
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })







