# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Comment(models.Model):
    #user = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

