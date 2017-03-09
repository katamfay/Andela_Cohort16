
from urllib.request import url
import json


def find_movie():

	Movies = "https://www.themoviedb.org/"
	request_movie = urlopen(Movies)
	Find_Movie = request_movie.read().decode("https://www.themoviedb.org/")
	json_object = json.loads(Find_Movie)
	print(json.dumps(json_objects))

find_movie()	