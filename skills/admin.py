from django.contrib import admin
from skills.models import Skill, SkillData
# Register your models here.

class SkillDataTabularInline(admin.TabularInline):
  model = SkillData

class SkillModelAdmin(admin.ModelAdmin):
  inlines = [SkillDataTabularInline]

  class Meta:
    model = Skill
admin.site.register(Skill, SkillModelAdmin)


