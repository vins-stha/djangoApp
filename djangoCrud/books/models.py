# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length = 40)
    book_price = models.IntegerField()
    book_publish = models.DateField(null = True)
    #book_author_id = ForeignKey author_id from authors table
    book_author = models.CharField(max_length = 40, null = True)
