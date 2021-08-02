from django.db import models
from embed_video.fields import EmbedVideoField





class Video(models.Model):

    video = EmbedVideoField()  # same like models.URLField()



class GameVideo(models.Model):
    game_video = EmbedVideoField()  # same like models.URLField()





class Channel(models.Model):
    channel_logo = models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    channel_desc= models.CharField(max_length=100)


class Game(models.Model):
    gamevideo = EmbedVideoField() 

class Discord(models.Model):
    discordvideo = EmbedVideoField()



class feedback(models.Model):
    name = models.CharField(max_length=122)
    feedback_desc= models.TextField()
    def __str__(self):
        return self.name 

class Check(models.Model):
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.password 
    