import webbrowser

class Entertain():
	def __init__(self, title, trailer_youtube_url, duration):
		self.title = title
		self.trailer_youtube_url = trailer_youtube_url
		self.duration = duration

class Movie(Entertain):
	def __init__(self, title, trailer_youtube_url, duration, storyline, poster_image_url, 
					actor, director, data_release):
		Entertain.__init__(self, title, trailer_youtube_url, duration)

		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.actor = actor
		self.director = director
		self.data_release = data_release

	def show_trailer(self):
		webbrowser.open(self.poster_image_url)

class Music(Entertain, object):
	def __init__(self, title, trailer_youtube_url, duration, author, performer, category):
		Entertain.__init__(self, title, trailer_youtube_url, duration)

		self.author = author
		self.performer = performer
		self.category = category

	# The two functions help different sorting ways:
	def __repr__(self):
		return '{}: {} {} {} {} {} {}'.format(self.__class__.__name__,
						self.title, self.author, self.performer, 
						self.trailer_youtube_url, self.duration, self.category)

	def __cmp__(self, other):
		if hasattr(other, 'getKey'):
			return self.getKey().__cmp__(other.getKey())

