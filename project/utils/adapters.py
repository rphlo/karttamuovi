from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from rest_framework.response import Response

class CustomAccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_FRONT + \
            '/verify-email/' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
    
    def respond_email_verification_sent(self, request, user):
        return Response({'message': 'confirmation email sent'})