import datetime

from django.db import models


def getToken(login):
    return login + str(datetime.datetime.now())[:19]


class User(models.Model):
    login = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    firstNM = models.CharField(max_length=20, blank=True)
    secondNM = models.CharField(max_length=20, blank=True)
    token = models.CharField(max_length=40, blank=True)
    userRole = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return f'{self.login} {self.password} {self.token}'


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    photoLink = models.CharField(max_length=255, blank=False)
    speed = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    userId = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    articleNumber = models.IntegerField(default=0)
    flightTime = models.IntegerField(default=0)
    range = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    maxWind = models.IntegerField(default=0)
    maxAltitude = models.IntegerField(default=0)
    minAltitude = models.IntegerField(default=0)
    motorsNumber = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}, {self.speed}, ' \
               f'{self.flightTime}, {self.range}, ' \
               f'{self.weight}, {self.maxWind}, ' \
               f'{self.maxAltitude}, {self.minAltitude} '


class News(models.Model):
    name = models.CharField(max_length=255, blank=False)
    photoLink = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    date = models.CharField(max_length=1024, blank=True)
    type = models.IntegerField(default=0)
    userId = models.IntegerField(default=0)


class Worker(models.Model):
    firstNM = models.CharField(max_length=20, blank=False)
    secondNM = models.CharField(max_length=20, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.secondNM} {self.firstNM}'


class Message(models.Model):
    text = models.CharField(max_length=1024, blank=True)
    date = models.CharField(max_length=40, blank=True)
    chatName = models.CharField(max_length=40, blank=True)
    userLogin = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return f'{self.text} {self.date}'


class Chat(models.Model):
    firstUserLogin = models.CharField(max_length=40, blank=True)
    secondUserLogin = models.CharField(max_length=40, blank=True)
    status = models.IntegerField(default=0)
    chatName = models.CharField(max_length=40, blank=True)
    firstUserName = models.CharField(max_length=40, blank=True)
    chatTitle = models.CharField(max_length=40, blank=True)
    secondUserName = models.CharField(max_length=40, blank=True)
