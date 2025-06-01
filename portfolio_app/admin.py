from django.contrib import admin
from .models import Certification, Project, Testimonial, ContactSubmission, Skill

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
     list_display = ('title', 'issuing_organization', 'date_achieved', 'credential_id')
     list_filter = ('date_achieved', 'issuing_organization')
     search_fields = ('title', 'issuing_organization', 'credential_id', 'description')
     fields = ('title', 'issuing_organization', 'date_achieved', 
              'credential_id', 'credential_url', 'image', 'description')
     readonly_fields = ('date_achieved',)
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_position')
    search_fields = ('client_name', 'content')
    fields = ('client_name', 'client_position', 'content', 'avatar')

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'topic', 'submitted_at')
    list_filter = ('topic', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'message')
    readonly_fields = ('submitted_at',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage')
    search_fields = ('title', 'description')
    fields = ('title', 'percentage', 'description')