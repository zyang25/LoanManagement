#from wiselead.celery import app
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse

def send_verification_email(user_id):
    Account = get_user_model()
    try:
        user = Account.objects.get(pk=user_id)
        send_mail(
            'Please verify your account',
            'Follow this link to verify your account: \n' + 
                'http://localhost:8000{0}'.format(reverse('account-verify', kwargs={'uuid': str(user.verification_uuid)})),
            'from@wiselead.dev',
            [user.email],
            fail_silently=False,
        )
    except Exception as e:
        print("Reason: {0} UserId: {1}".format(e, user_id))