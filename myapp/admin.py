from django.contrib import admin
from .models import users,languages,projects,assign_language
# Register your models here.
admin.site.register(users)
admin.site.register(languages)
admin.site.register(projects)
admin.site.register(assign_language)