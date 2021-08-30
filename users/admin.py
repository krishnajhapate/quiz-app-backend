from django.contrib import admin
from users.models import User
from .forms import UserCreationForm
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    list_display = ("email","name","user_type")
    ordering = ("email",)

    
    

admin.site.register(User,UserAdmin)
