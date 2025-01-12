from django.db import models

# Skill model
class Skill(models.Model):
    short_description = models.TextField('Short Description', blank=False, null=False)

    def __str__(self):
        return f"id :{self.short_description}"

# SkillData model
class SkillData(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True, related_name='data')  # Updated related_name
    language = models.CharField('Language', max_length=20)
    knowledge = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.skill}"  # Updated field to reference the skill
