from django.contrib import admin

from team.models import Member, Team

# Register your models here.
class TeamMemberInline(admin.TabularInline):
    model = Team.members.through
    extra = 1
    fields = ['member']

class MemberTeamInline(admin.TabularInline):
    model = Member.teams.through
    extra = 1
    fields = ['team']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [TeamMemberInline]
    exclude = ['members']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    inlines = [MemberTeamInline]

