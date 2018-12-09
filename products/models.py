from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	image = models.FileField(upload_to = 'images/')
	icon = models.FileField(upload_to = 'images/')
	votes_total = models.IntegerField(default = 1)
	body = models.TextField()
	url = models.TextField()
	hunter = models.ForeignKey(User, on_delete = models.CASCADE)


	def summary(self):
		return self.body[:100]

	def beautify_pub_date(self):
		return self.pub_date.strftime('%b %e, %Y ')

	def __str__(self):
		return f'{self.title}'