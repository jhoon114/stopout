from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.school_name}'


class Student(models.Model):
    pass