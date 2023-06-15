from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.CharField(max_length=100, blank=True, null=True)
    total_members = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class CommunityOwners(models.Model):
    community = models.ForeignKey('community.Community', on_delete=models.CASCADE)
    user = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
