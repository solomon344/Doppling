from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
import os
from django.conf import settings


def send_login_email_OTP(to:list,otp:str,subject:str):
    html_message = render_to_string("otp.html",context={'otp':otp})

    with mail.get_connection() as connection:
        email = mail.EmailMultiAlternatives(
        subject=subject,from_email='Doppling',to=to,connection=connection,
        )

        email.attach_alternative(html_message,'text/html')
        email.send()
    

def send_reset_password_link(link_to_reset,subject:str,to:list):
    html_message = render_to_string("otp.html",context={'reset_link':link_to_reset})

    with mail.get_connection() as connection:
        email = mail.EmailMultiAlternatives(
        subject=subject,from_email='Doppling',to=to,connection=connection,
        )

        email.attach_alternative(html_message,'text/html')
        email.send()

def send_welcom_email(to:list,get_started_link:str,subject):
    html_message = render_to_string("welcome_email.html",context={'get_started_link':get_started_link})

    with mail.get_connection() as connection:
        email = mail.EmailMultiAlternatives(
        subject=subject,from_email='Doppling',to=to,connection=connection,
        )

        email.attach_alternative(html_message,'text/html')
        email.send()



def send_verify_email_link(verify_link,subject:str,to:list):
    html_message = render_to_string("reset_password.html",context={'verify_link':verify_link})

    with mail.get_connection() as connection:
        email = mail.EmailMultiAlternatives(
        subject=subject,from_email='Doppling',to=to,connection=connection,
        )

        email.attach_alternative(html_message,'text/html')
        email.send()