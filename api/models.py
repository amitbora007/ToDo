from django.db import models

# Create your models here.
class ToDo(models.Model):
	todo = models.CharField(max_length=250)
	comment = models.CharField(max_length=250)
	reply = models.CharField(max_length=250)
	status =models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	end = models.DateTimeField()
	updated = models.DateTimeField(auto_now=True)
	
	
	def __str__(self):
		return self.todo
		
