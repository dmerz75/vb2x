from django.contrib import admin

# Register your models here.
from .models import VbRoundModel, Choice


# admin.site.register(VbRoundModel)
# class ChoiceInLine(admin.StackedInline):
#     model = VbRoundModel
#     extra = 3


class VbRoundAdmin(admin.ModelAdmin):
    # fields = ["num_players", "non_exclusions"] #, "non_excluded"]
    fieldsets = [
        (None, {"fields": ["num_players"]}),
        ("Parameters", {"fields": ["non_exclusions"],
                        "classes": ["collapse"]})]
    # inlines = [ChoiceInLine]
    # list_display = ["num_players", "non_exlcusions"]


# admin.site.register(Choice)
admin.site.register(VbRoundModel, VbRoundAdmin)

