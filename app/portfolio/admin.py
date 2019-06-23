from django.contrib import admin

from .models import Menu
from .models import Person
from .models import Email
from .models import Website
from .models import Phone
from .models import Education
from .models import WorkExperience
from .models import Publication
from .models import Project
from .models import Skill
from .models import Picture

admin.site.register(Menu)
admin.site.register(Person)
admin.site.register(Email)
admin.site.register(Website)
admin.site.register(Phone)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Picture)
