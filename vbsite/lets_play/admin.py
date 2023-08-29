from django.contrib import admin

# Register your models here.
from .models import Round


class RoundAdmin(admin.ModelAdmin):
    list_display = ["num_players", "non_exclusions", "created_at", "updated_at"]
    # fields = ["num_players", "non_exclusions"] #, "non_excluded"]
    # fieldsets = [
    #     (None, {"fields": ["num_players", "pub_date"]}),
    #     ("Parameters", {"fields": ["non_exclusions"],
    #                     "classes": ["collapse"]})]
    # inlines = [ChoiceInLine]
    # list_display = ["num_players", "non_exlcusions"]


# admin.site.register(Choice)
admin.site.register(Round, RoundAdmin)
