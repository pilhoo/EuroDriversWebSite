from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField()


class UserPlus(models.Model):
    ROLES = {
        ('S', 'Super Admin'),
        ('A', 'Admin'),
        ('T', 'Translator'),
        ('U', 'User'),      # TODO remove after Social Auth support done
    }
    role = models.CharField(max_length=1, choices=ROLES)
    lang = models.ForeignKey(Language)
    user = models.ForeignKey(User, related_name='roles')


class Post(models.Model):
    nr = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    lang = models.ForeignKey(Language)
    added = models.DateTimeField(auto_now_add=True)
    modififed = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='+')
    translator = models.ForeignKey(User, related_name='+')


#class Comment(models.Model):
    ## TODO
    #pass
