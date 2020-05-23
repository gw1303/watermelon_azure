
import os, sys
 
sys.path.append('/home/gw1303/watermelon/watermelon_project')
sys.path.append('/home/gw1303/watermelon/watermelon_venv/lib/python3.5/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"]="watermelon_project.settings"

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
    print('importing')
    from django.core.cache import cache
    print('succes')
except :
    print(traceback.print_exc())



# # model cache data setting
# model_cache_key = 'model_cache' 

# model = cache.get(model_cache_key) # get model from cache

# if model is None:
#     # your model isn't in the cache so `set` it
#     try :
#         print('model loading')
#         # 모델 불러오기
#         model = Word2Vec.load('/home/gw1303/watermelon/song2vec/song2vec.model')
#         print('model success')
#         cache.set(model_cache_key, model, None) # save in the cache
#         # in above line, None is the timeout parameter. It means cache forever

#     except :
#         print('error')
#         print(traceback.print_exc()) # load model
    
# songDf cache data setting
# songDf_cache_key = 'songDf_cache' 

# songDf = cache.get(songDf_cache_key) # get model from cache

# if songDf is None:
#     try :
#         print('songDf loading')
#         # song meta data
#         songDf = pd.read_json('/home/gw1303/watermelon/data/song_meta.json', encoding='utf-8')
#         print('songDf success')
#         cache.set(songDf_cache_key, songDf, None) # save in the cache
        

#     except :
#         print('error')
#         print(traceback.print_exc())


# try :
#     print('playlistDf loading')
#     # 플레이리스트 df
#     playlistDf = pd.read_json('/home/gw1303/watermelon/data/train.json', encoding='utf-8')
#     print('playlistDf success')

# except :
#     print('error')
#     print(traceback.print_exc())

# try :
#     print('genreDf loading')
#     # 전체장르 종류 df
#     genreDf = pd.read_json('/home/gw1303/watermelon/data/genre_gn_all.json', typ='series', encoding='utf-8')
#     genreDfIndex = list(genreDf.index)
#     genreDfIndex
#     print('genreDf success')

# except :
#     print('error')
#     print(traceback.print_exc())


# try :
#     print('tag loading')
#     tag = []
#     for i in playlistDf.tags :
#         tag += i
#     tagUnique = list(set(tag))
#     print('tag success')

# except :
#     print('error')
#     print(traceback.print_exc())







# Create your views here.
def keyboard(request):
    return JsonResponse({
	    'test': 'ok'    })

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


