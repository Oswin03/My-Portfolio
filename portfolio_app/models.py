from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200, default="Self-issued")  # ✅ default added here
    date_achieved = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='certifications/', 
        blank=True, 
        null=True,
        help_text="Upload a high-quality image of your certification"
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_achieved']
        verbose_name_plural = "Certifications"

    def __str__(self):
        return f"{self.title} ({self.issuing_organization})"


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to='projects/',
        help_text="Upload a project screenshot or cover image"
    )
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    technologies = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    avatar = models.ImageField(
        upload_to='testimonials/', 
        blank=True, 
        null=True,
        help_text="Client profile picture"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.client_name} ({self.client_company or self.client_position})"


class ContactSubmission(models.Model):
    TOPIC_CHOICES = [
        ('general', 'General Inquiry'),
        ('project', 'Project Collaboration'),
        ('job', 'Job Opportunity'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES)
    message = models.TextField()
    accepted_terms = models.BooleanField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name_plural = "Contact Submissions"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_topic_display()}"


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    percentage = models.IntegerField(
        help_text="Skill percentage (0-100)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    icon = models.CharField(
        max_length=50, 
        default='fas fa-star',
        help_text="Font Awesome icon class (e.g., 'fas fa-code')"
    )
    is_technical = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-percentage']
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.title} ({self.percentage}%)"
