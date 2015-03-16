DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edu_api',
        'USER': 'amillspaugh',
        'PASSWORD': 'knew1for!',
        'HOST': 'dept-of-edu.cvqqp54rm4vr.us-east-1.rds.amazonaws.com',
        'PORT': 3306,
    }
}