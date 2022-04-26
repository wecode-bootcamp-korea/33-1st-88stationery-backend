from django.db    import models
from tkinter      import CASCADE
from users.models import User

class Question(models.Model):
    title      = models.CharField(max_length=50)
    detail     = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'questions'

class Answer(models.Model):
    writer     = models.CharField(max_length=30)
    detail     = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    question   = models.ForeignKey('Questions', on_delete=models.CASCADE)

    class Meta:
        db_table = 'answers'