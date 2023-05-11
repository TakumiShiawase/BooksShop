from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Book(models.Model):
	writer = models.ForeignKey()
	category = models.ForeignKey(Genre, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	price = models.IntegerField()
	coverpage = models.FileField(upload_to = "#")
	bookpage = models.FileField(upload_to = "#")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	totalreview = models.IntegerField(default=0)
	totalrating = models.IntegerField(default=0)
	status = models.IntegerField(default=0)
	description = models.TextField()
	

	
class Users(models.Model):
	name = models.CharField(max_length = 100)
	user_dis = models.TextField()
	user_avatar = models.FileField(upload_to = "#")
	create_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)
	user_rating = models.IntegerField()

	def __str__(self):
		return self.name
	
class Review(models.Model):
	autor = models.ForeignKey(Users, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_rating = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
