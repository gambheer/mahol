from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
