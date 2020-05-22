import pandas as pd
from gensim.models import Word2Vec

songDf = pd.read_json('home/gw1303/watermelon/data/song_meta.json', encoding='utf-8')

# 대문자 -> 소문자
for i in ['album_name', 'song_name', 'artist_name_basket'] :
    songDf[i] = songDf[i].map(str).map(str.lower)

# 플레이리스트 df
playlistDf = pd.read_json('home/gw1303/watermelon/data/train.json', encoding='utf-8')
playlistDf

# 모델 불러오기
model = Word2Vec.load('home/gw1303/watermelon/song2vec/song2vec.model')


def test() :
	return 'Hello'