from django.contrib import admin
from users.models import User
from .forms import UserCreationForm
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    list_display = ("email","name","user_type",)
    ordering = ("email",)

    fieldsets = (
        ('Personal Details',{
            "fields":('name','email',"phone","user_type")
        }),
    )
    add_fieldsets =(
        (None,
        {
            'classes':('wide',),
            'fields':('name','email','password','phone','user_type'),
            }),
    )
    

admin.site.register(User,UserAdmin)
