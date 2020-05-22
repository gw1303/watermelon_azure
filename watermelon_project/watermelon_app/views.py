from django.shortcuts import render



# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


import pandas as pd
from watermelon_app.models import (songDf, playlistDf)


from gensim.models import Word2Vec
model = Word2Vec.load('home/gw1303/watermelon/song2vec/song2vec.model')


# Create your views here.
def keyboard(request):

    return JsonResponse({
        'type': 'text',
	    'test': 't.test()'
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
