from django.shortcuts import render, get_object_or_404
#from django.http import Http404
# render is used to combine the render and loader functions
from .models import Album, Song
#from django.template import loader 

def index(request):
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html')
	# now , we create a dictionary
	# to pass our album information to the template
	# contex is a variable
	context = {															
		'all_albums' : all_albums,
	}
	#return HttpResponse(template.render(context, request))

	return render(request, 'music/index.html', context)



	#note : In templates , we write python code in {% %} and variable in {{}}
	# html = ''
	# for album in all_albums:
	# 	url = '/music/'+ str(album.id) + '/'
	# 	html+='<a href="' + url + '">' + album.album_title + '</a><br>'
	

def detail(request, album_id):
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("Album does not exist")
	album = get_object_or_404(Album, pk = album_id)
	return render(request, 'music/detail.html', {'album':album})
	#we can either use {'album':album} or assign it to a variable

	#return HttpResponse("<h2>Details for Album ID: " +str(album_id) +" </h2>")	



def favorite(request, album_id):
	album = get_object_or_404(Album, pk = album_id)
	try:
		select_song = album.song_set.get(pk = request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {'album' : album , 'error_message' : "You did not select a valid song"})
	else:
		selected_song.is_favorite = True
		selected_song.save()	
		return render(request, 'music/detail.html', {'album':album})
