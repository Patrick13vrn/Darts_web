from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


class Throw(models.Model):
    player = models.CharField(max_length=10, db_index=True, blank=True)
    throw_code = models.CharField(max_length=10, db_index=True, blank=True)
    throw_k = models.CharField(max_length=10, db_index=True, blank=True)
    throw_v = models.CharField(max_length=10, db_index=True, blank=True)
    game = models.CharField(max_length=10, db_index=True, blank=True)
    set = models.CharField(max_length=10, db_index=True, blank=True)
    leg = models.CharField(max_length=10, db_index=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
