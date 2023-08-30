from django.contrib import admin
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from food.models import Profile
# Register your models here.
admin.site.register(Profile)