from django.shortcuts import render
from django.utils import timezone
from .models import Job

def jobs_list(request):
    jobs = Job.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(request, 'app/jobs_list.html', {'jobs': jobs})
