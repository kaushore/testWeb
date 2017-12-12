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

	def __str__(self):  # string representation of a class
		return self.album_title +'-'+self.artist


class Song(models.Model):  # in the shell, we can access the songs' set using album1.song_set.all().
						   # album1 is a variable of type Album and the we use the class name in lowerCase with _set.all()
						   # we can add songs using album1.song_set.create(song_title='xx', file_type = 'mp3')
	album = models.ForeignKey(Album, on_delete = models.CASCADE) 
	# ForeignKey is used to associate a song to an Album through the primary key of the album 
	# on_delete : if anf album is deleted, then go ahead and delete the corresponding songs
	file_type = models.CharField(max_length = 10)
	song_title = models.CharField(max_length = 250)
	is_favourite = models.BooleanField(default = False)

	def __str__(self):
		return self.song_title
