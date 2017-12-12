# 3 steps :
# 1.  make changes in the database(models)
# 2. run the make migrations command
# 3. run the migrate
# to edit : python manage.py shell

from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=250)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

	def __str__(self):  # string representation of an object
		return self.album_title +'-'+self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE) 
	# ForeignKey is used to associate a song to an Album through the primary key of the album 
	# on_delete : if anf album is deleted, then go ahead and delete the corresponding songs
	file_type = models.CharField(max_length = 10)
	song_title = models.CharField(max_length = 250)
