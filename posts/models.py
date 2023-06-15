from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    type = models.CharField(max_length=20, blank=False, null=False)
    content = models.CharField(max_length=500, blank=False, null=False)
    user_id = models.IntegerField(max_length=8, blank=False, null=False)
    community_id = models.IntegerField(max_length=8, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
