from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Job
from .forms import JobForm

def jobs_list(request):
    jobs = Job.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(request, 'app/jobs_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'app/job_detail.html', {'job': job})

def job_new(request):
    form = JobForm()
    return render(request, 'app/job_new.html', {'form': form})
