from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ImageField(upload_to='uploads/', max_length=500)
    status = models.IntegerField(max_length=4, null=False, blank=False)  # active=1, inactive=0, new=2
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class CommunityMembers(models.Model):
    community = models.ForeignKey('community.Community', on_delete=models.CASCADE)
    user = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    role = models.IntegerField(max_length=4, blank=False, null=False)  # admin=1, member=2
    status = models.IntegerField(max_length=4, blank=False, null=False)  # requested=0, active=1, inactive=2
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommunityQam(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    community = models.ForeignKey('community.Community', on_delete=models.CASCADE)
    link = models.CharField(max_length=100, blank=False, null=False)
    status = models.IntegerField(max_length=4, blank=False, null=False)  # active=1, inactive=0, deleted=2
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
