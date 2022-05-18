from django.db import models
from django.conf import settings
from django.utils import timezone

class Job(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    # company = models.ForeignKey(on_delete=models.CASCADE)
    open = models.BooleanField(default=True)
    def publish(self):
        self.published_at = timezone.now()
        self.save()
    def __str__(self):
        return self.title
