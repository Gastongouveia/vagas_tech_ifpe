from django.db import models
from django.conf import settings
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"


class UserRole(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
    role = models.ForeignKey(Role, on_delete = models.SET_NULL, null = True)
    active = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user} - {self.role}"
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    def publish(self):
        self.published_at = timezone.now()
        self.save()
    def __str__(self):
        return self.name
    
class Job(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def publish(self):
        self.published_at = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    
    
class Technology(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserTechnology(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    time_experience = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.technology}"
    
class UserCompany(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    function = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.company}"
    
class UserJobs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.job}"
