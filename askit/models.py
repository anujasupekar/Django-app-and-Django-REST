from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=20)
	posted_by = models.CharField(max_length=20)
	post_date = models.DateTimeField(default=timezone.now())
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Answer(models.Model):
	question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE, null=True)
	answer = models.TextField()
	written_by = models.CharField(max_length=20)
	post_date = models.DateTimeField(null=True)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)

	def __str__(self):
		return self.answer