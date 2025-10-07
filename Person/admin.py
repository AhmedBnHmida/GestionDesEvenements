from django.contrib import admin
from .models import Person

class ResearchPerson(admin.ModelAdmin):
    search_fields = ['user__username']  # Si vous utilisez OneToOneField avec User
    # OU search_fields = ['username']  # Si vous utilisez AbstractUser
    
    list_display = ['cin', 'email', 'get_username']
    
    def get_username(self, obj):
        return obj.user.username  # Si OneToOneField
        # return obj.username  # Si AbstractUser
    get_username.short_description = 'Username'

admin.site.register(Person, ResearchPerson)