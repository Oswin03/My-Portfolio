from django import forms
from .models import ContactSubmission

TOPIC_CHOICES = [
    ('general', 'General Inquiry'),
    ('project', 'Project Collaboration'),
    ('other', 'Other'),
]

class ContactForm(forms.ModelForm):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    accepted_terms = forms.BooleanField(required=True, label="I accept the Terms")
    
    class Meta:
        model = ContactSubmission
        fields = ['first_name', 'last_name', 'email', 'phone', 'topic', 'message', 'accepted_terms']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }