from django.shortcuts import render



# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


import pandas as pd
from watermelon_app.models import (songDf, playlistDf)


def __init__(request) :
    # song meta data
    songDf = pd.read_json('home/gw1303/watermelon/data/song_meta.json', encoding='utf-8')

    # 대문자 -> 소문자
    for i in ['album_name', 'song_name', 'artist_name_basket'] :
        songDf[i] = songDf[i].map(str).map(str.lower)

    # 플레이리스트 df
    playlistDf = pd.read_json('home/gw1303/watermelon/data/train.json', encoding='utf-8')
    playlistDf

    # 모델 불러오기
    model = Word2Vec.load('home/gw1303/watermelon/song2vec/song2vec.model')


# Create your views here.
def keyboard(request):

    return JsonResponse({
        'type': 'text',
	    'test': 'test ok'
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


def getSongId(request) :

    # 사용자 입력 
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    userSongName = str(return_str).strip()

    userSongName = userSongName.lower()

    if userSongName == '아이유' :
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': songDf['song_name'][1]
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })


