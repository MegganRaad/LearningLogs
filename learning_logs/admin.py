from django.contrib import admin
# implement code here to register Topic code with the admin site
from .models import Topic

admin.site.register(Topic)
