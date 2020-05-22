from django.db import models


class songDf(models.Model) :
	song_gn_dtl_gnr_basket = models.CharField(max_length=200)

	issue_date = models.IntegerField(default=1)

	album_name = models.CharField(max_length=200)

	lbum_id = models.IntegerField(default=1)

    artist_id_basket = models.CharField(max_length=200)

    song_name = models.CharField(max_length=200)

    song_gn_gnr_basket = models.CharField(max_length=200)

    artist_name_basket = models.CharField(max_length=200)

    id = models.IntegerField(default=1)


class playlistDf(models.Model) :
	tags = models.CharField(max_length=200)

	id = models.IntegerField(default=1)

	plylst_title = models.CharField(max_length=200)

	songs = models.CharField(max_length=200)

	like_cnt = models.IntegerField(default=1)

	updt_date = models.CharField(max_length=200)
# Create your models here.


