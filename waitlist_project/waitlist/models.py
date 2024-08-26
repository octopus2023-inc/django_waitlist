from django.db import models

# waitlist/models.py

from django.db import models

class WaitlistEntry(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
 # waitlist/models.py

 # ... (existing code)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=WaitlistEntry)
def send_auto_reply(sender, instance, created, **kwargs):
     if created:
         subject = 'Thank you for joining our waitlist!'
         message = 'Thank you for joining our waitlist. We will keep you updated!'
         from_email = 'octopus2023.contact@8053878.m-sender-sib.com'  # Replace with your email address
         recipient_list = [instance.email]

         send_mail(subject, message, from_email, recipient_list)


