from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='uploads/', max_length=500)
    token = models.CharField(max_length=100, blank=False, null=False)
    role = models.IntegerField(max_length=4, blank=False, null=False)  # admin=1, super_admin=2, user=3
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
