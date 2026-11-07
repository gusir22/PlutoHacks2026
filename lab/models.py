"""Entirely fictional training data; no real user accounts."""
from django.db import models
class Employee(models.Model):
 name=models.CharField(max_length=80)
 username=models.CharField(max_length=40,unique=True)
 employee_number=models.IntegerField(unique=True)
 private_note=models.TextField(blank=True)
 is_public=models.BooleanField(default=False)
class Document(models.Model):
 title=models.CharField(max_length=100)
 body=models.TextField()
 is_public=models.BooleanField(default=True)
class Comment(models.Model):
 author=models.CharField(max_length=40)
 message=models.TextField(max_length=800)
