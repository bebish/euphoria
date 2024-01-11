from django.dispatch import receiver
from djoser.signals import user_registered
from django.core.mail import send_mail

@receiver(user_registered)
def send_welcome_email(sender, user, request, **kwargs):
    subject = 'Добро пожаловать!'
    message = 'Спасибо за регистрацию на нашем сайте.'
    from_email = 'euphoria@gmail.com'
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email)
