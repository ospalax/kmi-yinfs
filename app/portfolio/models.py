from django.db import models
from .validators import validate_skill_level

class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    order = models.IntegerField('Menu item order', default=0)
    def __str__(self):
        return self.menu_item

class Content(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    markup = models.TextField()
    def __str__(self):
        return self.menu_item + '_Content'

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    titles_before_name = models.CharField(max_length=30, blank=True)
    titles_after_name = models.CharField(max_length=30, blank=True)
    about_me = models.TextField()
    default_email = models.EmailField()
    default_website = models.URLField('My website', blank=True)
    default_phone = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name + \
            ' (' + self.default_email + ')'

class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField()
    def __str__(self):
        return self.email

class Website(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    website = models.URLField()
    def __str__(self):
        return self.website

class Phone(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone = models.CharField(max_length=60)
    def __str__(self):
        return self.phone

class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=100)
    institute_type = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateField('Education starting date')
    end_date = models.DateField('Education ending date', blank=True)
    def __str__(self):
        return self.institute_name + ' (' + self.institute_type + ')'

class WorkExperience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=500)
    start_date = models.DateField('Job start date')
    end_date = models.DateField('Job end date', blank=True)
    def __str__(self):
        return self.job_title + ' (' + self.company_name + ')'

class Publication(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField('Publication title', max_length=100)
    description = models.CharField('Publication summary', max_length=500)
    release_date = models.DateField('Publication date')
    def __str__(self):
        return self.title + ' (' + self.release_date + ')'

class Project(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=500)
    website = models.URLField(blank=True)
    def __str__(self):
        return self.project_name

class Skill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    skill_category = models.CharField(max_length=100)
    skill_level = models.PositiveSmallIntegerField(
        validators=[validate_skill_level])
    website = models.URLField(blank=True)
    def __str__(self):
        return self.skill_name + ' (' + self.skill_category + ')'

class Picture(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # file will be saved to MEDIA_ROOT/gallery/<year>/
    upload = models.ImageField(upload_to='gallery/%Y/')

