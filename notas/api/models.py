from django.db import models


class Nota(models.Model):
    body = models.CharField(null=True, blank=True,max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
