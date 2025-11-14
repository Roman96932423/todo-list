from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email')
    readonly_fields = ("last_login", "username", "date_joined")
    exclude = ("password", )
