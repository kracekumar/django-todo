# -*- coding: utf-8 -*-

import datetime
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=100)
    gravatar_url = models.URLField(max_length=150, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        msg = u"active"
        if not self.active:
            msg = u"inactive"
        return u"{username} ({email}) is {msg}".format(
            username=self.username, email=self.email, msg=msg)


class NameMixin(models.Model):
    name = models.CharField(max_length=250)
    url_name = models.CharField(max_length=260)

    class Meta:
        abstract = True

    def make_url_name(self):
        if self.id is None:
            obj = self.__class__.objects.last()
            if obj:
                self.id = obj.id + 1
            else:
                # When table is empty we need put id as 1
                self.id = 1
        self.url_name = u"{id}-{name}".format(
            id=self.id,
            name=self.name.lower().replace(" ", "-")
        )


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(
        default=datetime.datetime.now, auto_now=True)

    class Meta:
        abstract = True


class Bucket(NameMixin, DateTimeMixin):
    user = models.ForeignKey('User', related_name=u"user")

    def save(self, *args, **kwargs):
        self.make_url_name()

        super(Bucket, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{name} by {username} has {total} tasks".format(
            name=self.name, username=self.user.username,
            total=self.task.count()
        )


class Task(NameMixin, DateTimeMixin):
    description = models.TextField()
    bucket = models.ForeignKey('Bucket', related_name=u"task")
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        msg = u"not completed"
        if self.completed:
            msg = u"completed"
        return u"{name} is {msg}".format(name=self.name, msg=msg)
