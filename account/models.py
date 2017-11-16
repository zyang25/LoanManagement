from django.db import models
from django.db.models import signals
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from .tasks import send_verification_email

# Create your models here.
class UserAccountManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')
 
        if not password:
            raise ValueError('Password must be provided')
 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
 
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
 
    objects = UserAccountManager()
 
    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('full name', blank=True, null=True, max_length=400)
    cell_phone = models.CharField('cell phone', blank=False, null=False, max_length=11)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_verified = models.BooleanField('verify', default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
 
    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.email

# Send email after user registration
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        #send_verification_email.delay(instance.pk)
        send_verification_email(instance.pk)

signals.post_save.connect(user_post_save, sender=Account)