import pandas as pd
import numpy as np
from konlpy.tag import Kkma
from konlpy.utils import pprint
from tqdm.notebook import tqdm
from tensorflow.keras.preprocessing.sequence import pad_sequences


from gensim.models import Word2Vec

# song meta data
songDf = pd.read_json('/home/gw1303/watermelon/data/song_meta.json', encoding='utf-8')

# 플레이리스트 df
playlistDf = pd.read_json('/home/gw1303/watermelon/data/train.json', encoding='utf-8')


# 전체장르 종류 df
genreDf = pd.read_json('/home/gw1303/watermelon/data/genre_gn_all.json', typ='series', encoding='utf-8')
genreDfIndex = list(genreDf.index)
genreDfIndex

tag = []
for i in playlistDf.tags :
    tag += i
    
tagUnique = list(set(tag))

# 모델 불러오기
model = Word2Vec.load('/home/gw1303/watermelon/song2vec/song2vec.model')

def test() :
	return songDf.iloc[10][3]









# 파일 올리기 
# pscp C:\Users\gw130\Desktop\multicampus\multicampus_project\음악추천_챗봇\data\* gw1303@13.68.191.35:/home/gw1303/watermelon/data