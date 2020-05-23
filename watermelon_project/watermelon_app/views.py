from django.shortcuts import render



# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json



# load_data
import pandas as pd
import numpy as np
from konlpy.tag import Kkma
from tqdm.notebook import tqdm
from tensorflow.keras.preprocessing.sequence import pad_sequences
from gensim.models import Word2Vec

import traceback

try :
    print('songDf loading')
    # song meta data
    songDf = pd.read_json('/home/gw1303/watermelon/data/song_meta.json', encoding='utf-8')
    print('songDf success')

except :
    print('error')
    print(traceback.print_exc())

try :
    print('playlistDf loading')
    # 플레이리스트 df
    playlistDf = pd.read_json('/home/gw1303/watermelon/data/train.json', encoding='utf-8')
    print('playlistDf success')

except :
    print('error')
    print(traceback.print_exc())

try :
    print('genreDf loading')
    # 전체장르 종류 df
    genreDf = pd.read_json('/home/gw1303/watermelon/data/genre_gn_all.json', typ='series', encoding='utf-8')
    genreDfIndex = list(genreDf.index)
    genreDfIndex
    print('genreDf success')

except :
    print('error')
    print(traceback.print_exc())


try :
    print('tag loading')
    tag = []
    for i in playlistDf.tags :
        tag += i
    tagUnique = list(set(tag))
    print('tag success')

except :
    print('error')
    print(traceback.print_exc())

try :
    print('model loading')
    # 모델 불러오기
    model = Word2Vec.load('/home/gw1303/watermelon/song2vec/song2vec.model')
    print('model success')

except :
    print('error')
    print(traceback.print_exc())





# Create your views here.
def keyboard(request):
    return JsonResponse({
	    'test': songDf.iloc[4,3]
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
