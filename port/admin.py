from django.contrib import admin
from .models import Profile
from .models import Work
from .models import Education

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Education)

# Register your models here.
