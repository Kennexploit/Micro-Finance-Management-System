from django.db import models


class applicant(models.Model):

	Your_name=models.CharField(max_length=100)
	Your_id = models.CharField(max_length=20)
	Your_contact=models.EmailField(max_length=100)
	Your_email=models.EmailField(max_length=100, default='+254')
	Amount=models.CharField(max_length=20)
	Date = models.DateTimeField(auto_now=True)
	

	def __str__(self):
		return self.Your_name
