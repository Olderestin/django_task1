from django.contrib import admin

from team.models import Member, Team

# Register your models here.
class TeamMemberInline(admin.TabularInline):
    """
    Inline admin class for Team members.
    
    This allows managing members directly from the Team admin page.
    """

    model = Team.members.through
    extra = 1
    fields = ['member']

class MemberTeamInline(admin.TabularInline):
    """
    Inline admin class for Member teams.
    
    This allows managing teams directly from the Member admin page.
    """

    model = Member.teams.through
    extra = 1
    fields = ['team']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """
    Admin class for the Team model.

    Provides a custom display in the Django admin interface for managing Team instances.
    """

    list_display = ['title', 'description']
    inlines = [TeamMemberInline]
    exclude = ['members']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Admin class for the Member model.

    Provides a custom display in the Django admin interface for managing Member instances.
    """
    
    list_display = ['first_name', 'last_name']
    inlines = [MemberTeamInline]

