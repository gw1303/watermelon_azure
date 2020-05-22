from django.shortcuts import render



# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


import pandas as pd
from watermelon_app.models import (songDf, playlistDf)


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

    # song meta data
    songDf = pd.read_json('home/gw1303/watermelon/data/song_meta.json', encoding='utf-8')

    # 대문자 -> 소문자
    for i in ['album_name', 'song_name', 'artist_name_basket'] :
        songDf[i] = songDf[i].map(str).map(str.lower)

    # 플레이리스트 df
    playlistDf = pd.read_json('home/gw1303/watermelon/data/train.json', encoding='utf-8')
    playlistDf


    # 사용자 입력 
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    userSongName = str(return_str).strip()


    userSongName = userSongName.lower()


    try :
        artist, song = userSongName.split('-')
    except ValueError :

        getSongId()

    # 입력받은 가수와 제목으로 df 구성
    findArtistDf = songDf[songDf.artist_name_basket.str.contains(artist.strip())].sort_values(by='song_name')
    if len(findArtistDf.song_name.str.replace(' ', '').str.contains(song.strip())) > 0 :

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

   #      findSongDf = findArtistDf[findArtistDf.song_name.str.replace(' ', '').str.contains(song.strip())]
   #  else :
   #      findSongDf = findArtistDf

   #  userSelect = 999999999
    
   #  # 검색된 노래가 2개 이상일 경우 선택받는다
   #  if len(findSongDf) > 1 :
   #      print('무슨 노래입니까 ?', end='\n\n')
   #      for i in range(len(findSongDf)) :
   #          song = findSongDf.iloc[i].song_name
   #          artist = findSongDf.iloc[i].artist_name_basket
   #          album = findSongDf.iloc[i].album_name
   #          print('%d 번 %s - %s   /   %s'%(i+1, song, artist, album), end='\n\n')
        
   #      while userSelect >= len(findSongDf) :
   #          userSelect = int(input('번호를 입력하시오.')) - 1
        
        
   #      print("\n%s 의 ['%s'] 곡이 추가되었습니다." %(findSongDf.iloc[userSelect].artist_name_basket,
   #                                        findSongDf.iloc[userSelect].song_name))
        
   #      return findSongDf.iloc[userSelect].id
   # # 검색된 노래가 하나일 경우 
   #  else :
   #      print("\n%s 의 ['%s'] 곡이 추가되었습니다." %(findSongDf.artist_name_basket.tolist()[0], findSongDf.song_name.tolist()[0]))
        
   #      return findSongDf.id.tolist()[0]