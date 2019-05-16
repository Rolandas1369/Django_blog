'''Change timezone in dajngo-blog/settings.py'''

LANGUAGE_CODE = 'Europe/Vilnius'

'''Static dir'''
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

'''If deploying'''
ALLOWED_HOSTS = ['127.0.0.1', 'something.com']

'''First migrations'''
python manage.py migrate

'''python manage.py startapp blog'''

'''Add to installed apps in settings'''
blog',

'''Model for blog'''

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''Making migrations'''
python manage.py makemigrations blog

'''Migrate'''
python manage.py migrate blog


'''Create admin register Post to see in admin'''

from django.contrib import admin
from .models import Post

admin.site.register(Post)

'''Create superuser'''
python manage.py createsuperuser