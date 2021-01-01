from django.shortcuts import render
from django.views.generic import View
from .models import Profile, Work, Education

class IndexView(View):
  def get(self, request, *args, **kwargs):
    profile_data = Profile.objects.all()
    if profile_data.exists():
      profile_data = profile_data.order_by('-id')[0]
    work_data = Work.objects.order_by('-id')
    return render(request, 'port/index.html',{
      'profile_data': profile_data,
      'work_data': work_data
    })
# Create your views here.

class DetailView(View):
  def get(self, request, *args, **kwargs):
    work_data = Work.objects.get(id=self.kwargs['pk'])
    return render(request, 'port/detail.html',{
        'work_data': work_data
    })

class AboutView(View):
  def get(self, request, *args, **kwargs):
    profile_date = Profile.objects.all()
    if profile_date.exists():
      profile_date = profile_date.order_by('-id')[0]
    education_data = Education.objects.order_by('-id')
    return render(request, 'port/about.html',{
      'profile_data': profile_date,
      'education_data': education_data,
    })
