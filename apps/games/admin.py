from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from games.models import Game, Screenshot


def short_description(obj, length=40):
    """Return the first ``length`` characters of the description."""
    return obj.description[0:length]


class ScreenshotInline(admin.StackedInline):
    model = Screenshot
    readonly_fields = ('game', 'file')
    extra = 0


class GameAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'creator', 'url', short_description, 'is_approved')
    list_filter = ('is_approved',)
    prepopulated_fields = {'slug': ('name',)}
    actions = ['approve_games', 'reject_games', 'unreview_games']
    inlines = [ScreenshotInline,]

    def approve_games(self, request, queryset):
        queryset.update(is_approved=True, reviewed_by=request.user)

    def unreview_games(self, request, queryset):
        queryset.update(is_approved=None, reviewed_by=None)

    def reject_games(self, request, queryset):
        queryset.update(is_approved=False, reviewed_by=request.user)


class ScreenshotAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
