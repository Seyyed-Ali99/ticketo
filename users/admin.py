from django.contrib import admin
from .models import SUser

# Register your models here.

@admin.register(SUser)
class SUserAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "national_id",
        "passport_id",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "role",
    )
    ordering = ("-id",)
    list_per_page = 10
    search_fields = ("national_id","passport_id","email","phone_number","role",)
    list_filter = ("role",)
