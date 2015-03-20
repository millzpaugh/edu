
DEBUG = False
TEMPLATE_DEBUG = False



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'edu',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edu_api',
        'USER': 'ebroot',
        'PASSWORD': 'knew1for!',
        'HOST': 'dept-of-edu.cvqqp54rm4vr.us-east-1.rds.amazonaws.com',
        'PORT': 3306,
    }
}
