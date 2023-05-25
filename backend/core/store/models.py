from django.db import models
from django.contrib.auth import get_user_model

class Genre(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Book(models.Model):
	writer = models.CharField(max_length=50)
	genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	price = models.IntegerField()
	coverpage = models.ImageField(upload_to='book_images', default='default_book_img.png')
	# bookpage = models.FileField(upload_to = "#")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	totalreview = models.IntegerField(default=0)
	totalrating = models.IntegerField(default=0)
	status = models.IntegerField(default=0)
	description = models.TextField()
#	favourite = models.ManyToManyField(User, related_name='favourite', blank=True)



class Review(models.Model):
	#autor = models.ForeignKey(Users, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_rating = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    #user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    taken = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Comment by {self.user} on {self.book}'