# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
