import pandas as pd


genreDf = pd.read_json('home/gw1303/watermelon/data/genre_gn_all.json', encoding='utf-8')


def test() :
	return genreDf.iloc[0]