from django.db import models
# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=40)
    emailid=models.CharField(primary_key=True,max_length=40)
    password=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.emailid}"

class interest(models.Model):
    emailid=models.ForeignKey(to=user,on_delete=models.CASCADE)
    interest=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.interest}"

class questions(models.Model):
    iid = models.ForeignKey(to=interest,on_delete=models.CASCADE)
    question=models.CharField(max_length=140)
    # Time_and_date=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.question}"
