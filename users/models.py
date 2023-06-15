from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100, blank=True, default=None)
    email = models.CharField(max_length=100, blank=True, default=None)
    phone = models.CharField(max_length=100, blank=False, null=False)
    token = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
