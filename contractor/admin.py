from django.contrib import admin
from .models import work, worker
from contractor.models import UserProfile
# Register your models here.
admin.site.register(work)
admin.site.register(worker)
admin.site.register(UserProfile)

