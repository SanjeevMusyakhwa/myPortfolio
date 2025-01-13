from django.shortcuts import render
from django.views.generic import TemplateView
from profile_app.models import Home
from about.models import About
from services.models import Service
from skills.models import Skill
from portfolio.models import Protfolio
# Create your views here.

class HomeView(TemplateView):
  template_name = 'index.html'
  
  def get_profile_obj(self,*args, **kwargs):
    profile_obj = Home.objects.first()
    return profile_obj
  
  def get_about_obj(self, *args, **kwargs):
   obj = About.objects.first()
   return obj
  
  def get_service_obj(self, *args, **kwargs):
    obj = Service.objects.all()
    return obj
  
  def get_skill_obj(self, *args, **kwargs):
    skill_obj = Skill.objects.first()
    if not skill_obj:
      return {'skill': None, 'skilldata': []}
    skills = {
      'skill': skill_obj,
      'skilldata': skill_obj.data.all()
  }
    return skills
  
  def get_portfolio_obj(self,*args, **kwargs):
    portfolio_obj = Protfolio.objects.all().order_by('-created_at')
    return portfolio_obj
  
  
  def get_context_data(self, **kwargs):
    context = super(HomeView,self).get_context_data(**kwargs)
    context['profile_objs'] = self.get_profile_obj()
    context["about_objs"] = self.get_about_obj()
    context["service_objs"] = self.get_service_obj()
    context['skills'] = self.get_skill_obj()
    context['portfolio_objs'] = self.get_portfolio_obj()
    return context