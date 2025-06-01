from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .models import Certification, Project, Skill  # Changed from Service to Certification
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certifications'] = Certification.objects.all().order_by('-date_achieved')[:4]  # Changed from services
        context['featured_projects'] = Project.objects.all()[:3]
        context['skills'] = Skill.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class CertificationsView(ListView):  # New view for certifications
    model = Certification
    template_name = 'certifications.html'
    context_object_name = 'certifications'
    ordering = ['-date_achieved']  # Show newest first
    paginate_by = 8

class ProjectsView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    ordering = ['-created_at']
    paginate_by = 6

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')

def expertise_view(request):
    skills = Skill.objects.all()
    return render(request, 'expertise.html', {'skills': skills})