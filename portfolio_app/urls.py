from django.urls import path
from .views import (
    HomeView,
    AboutView,
    CertificationsView,  # New import
    ProjectsView,
    expertise_view,
    contact_view,
    contact_success_view
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('certifications/', CertificationsView.as_view(), name='certifications'),  # New path
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('expertise/', expertise_view, name='expertise'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]