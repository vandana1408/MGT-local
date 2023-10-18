"""
Django settings for Mgt project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

SECRET_KEY = 'exo8nsf7fx&e@vs=#^-5)#$c%o^@8sm$$fu&3*%=g475o--ej_'

DEBUG = True

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '0.0.0.0', '[::1]', '*']

INSTALLED_APPS = [
	'Charger',
	'Clawclip',
    'django_tables2',
    'Home',
    'MGTdb_shared',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'rest_framework',
	'django_registration',
	'django_countries',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Mgt.urls_template' # CHANGE to new urls filename

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Home/templates/'), os.path.join(BASE_DIR, 'Home/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'Mgt.context_processors.root_url',
            ],
        },
    },
]

TEMPLATE_DEBUG = True

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
)

MANAGEMENT_COMMANDS = ['Mgt.management.commands.show_urls']

# MY_URL = "http://mgtdb.unsw.edu.au"
MY_URL = "http://127.0.0.1:8000"
WSGI_APPLICATION = 'Mgt.wsgi.application'

FILE_UPLOAD_PERMISSIONS=0o774
FILE_UPLOAD_DIRECTORY_PERMISSIONS=0o774

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 2018, Jan 9 - require a db router (if multiple databases)
NCBI_RETRIEVAL_FREQUENCY = {'Charger': None, 'Clawclip': None} # CHANGE

DATABASE_ROUTERS = ['Mgt.router.GenericRouter']
APPS_DATABASE_MAPPING = { 'Clawclip':'clawclip', 'Charger': 'charger' } #CHANGE change to appname in INSTALLED_APPS and database DATABASES in name normally upper and lowercase first letter i.e. Salmonella and salmonella

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "USER": 'blankuser',
        "PASSWORD": 'blankpassword',
        "HOST": "0.0.0.0",
        "PORT": "5432",
        'NAME': 'default',
    },
    # # 'blankdb': { #CHANGE postgres database name
    # #     'ENGINE': 'django.db.backends.postgresql',
    # #     'HOST': '0.0.0.0',
    # #     'PORT': '5432',
    # #     'USER': 'blankuser', #CHANGE add postgres user
    # #     'PASSWORD': 'blankpassword', #CHANGE add postgres password
    # #     'NAME': 'blankdb',#CHANGE to new database name
    # # },
    'charger': {
        "ENGINE": "django.db.backends.postgresql",
        "USER": 'blankuser',
        "PASSWORD": 'blankpassword',
        "HOST": "0.0.0.0",
        "PORT": "5432",
        'NAME': 'charger',
    },
    'clawclip': {
        "ENGINE": "django.db.backends.postgresql",
        "USER": 'blankuser',
        "PASSWORD": 'blankpassword',
        "HOST": "0.0.0.0",
        "PORT": "5432",
        'NAME': 'clawclip',
    },
}

NONLOCALHOST='0.0.0.0' # leave as 0.0.0.0 for local install

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# added_on: 2018, Feb 8 - for HMAC activation workflow
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window;
INCLUDE_REGISTER_URL = True
REGISTRATION_OPEN = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'mgtdb@babs.unsw.edu.au'
LOGIN_REDIRECT_URL = '/'


#RELATIVE PATHS FROM folder containing manage.py in this repo to folder on your system
SUBDIR_REFERENCES = './References/' #CHANGE location where reference genomes will be stored
SUBDIR_ALLELES = './Alleles/' #CHANGE location where allele sequences for the database will be stored
MEDIA_ROOT = './Uploads/'#CHANGE location where uploaded reads/allele files will be stored
BLASTALLELES='./species_specific_alleles/'#CHANGE location where initial allele sequences will be stored for read2allele

# ABSOLUTE PATH VERSIONS OF ABOVE
ABS_SUBDIR_REFERENCES = 'References/' #CHANGE location where reference genomes will be stored
ABS_SUBDIR_ALLELES = 'Alleles/' #CHANGE location where allele sequences for the database will be stored
ABS_MEDIA_ROOT = "Uploads/" #CHANGE location where uploaded reads/allele files will be stored
ABS_BLASTALLELES='species_specific_alleles/'#CHANGE location where initial allele sequences will be stored for read2allele

FILES_FOR_DOWNLOAD = "files_for_download/"#CHANGE replace path with storage location of allele and profile collections
TMPFOLDER = "tmp_files/"#CHANGE replace path with tmp specified in setup script

ASCPKEY = "/Path/to/.aspera/connect/etc/asperaweb_id_dsa.openssh"#CHANGE ONLY NEEDED IF RUNNING cron_pipeline --dl_reads

KRAKEN_DEFAULT_DB='/Path/to/folder/minikraken_20171013_4GB/'#CHANGE ONLY NEEDED IF RUNNING cron_pipeline --reads_to_alleles

### NOT NEEDED ON LOCAL DB ###
KATANA_LOCATION=''
TESTDB="True"
KATANA_SETTINGS=''
##############################

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

#CHANGE BELOW TO list species specific cutoffs/values
SPECIES_SEROVAR = {'Blankdb': {"species":'Blank species',
                                  "serovar":'',
                                  "min_largest_contig":60000,
                                  "max_contig_no":700,
                                  "n50_min":20000,
                                  "genome_min":4500000,
                                  "genome_max":5500000,
                                  "hspident":0.96,
                                  "locusnlimit":0.8,
                                  "snpwindow":40,
                                  "densitylim":4,
                                  "refsize":5.0,
                                  "blastident":90,
                                  "apzero":0.04
                                  }
                   }

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'Static/'

RAWQUERIES_DISPLAY = {'Clawclip': '', 'Charger': ''}

DB_USER='blankuser'
SETTING_FILE="/home/vandana/MGT-local/Mgt/Mgt/Mgt/settings_vp.py"
PATH_MGT="/home/vandana/MGT-local/"
SETTINGS_PREFIX="Mgt.settings_vp"
REFALLELES="species_specific_alleles/"
REF_FILES="tmp_setup_files/"
CONDAENV="mgtenv"
SUPERUSERNAME="blankblank1"
SUPERUSEREMAIL="blank1@blank1.blank1"


SETUP_DB = {
    'Charger': {
        # 'db_name': 'charger', # ALREADY IN PAGE  
        # 'app_name': 'Charger', # ALREADY IN PAGE  
        'species': '<i> Dell Laptop Charger </i>', # unique 
        'ref_genome':"/home/vandana/MGT-local/setup/example_inputs/genome.fasta", # unique 
        'lociloc':"/home/vandana/MGT-local/setup/example_inputs/lociLocationsInRef.txt", # unique
        'scheme_accessions':"/home/vandana/MGT-local/setup/example_inputs/Schemes", # unique 
        'schemeno':3, # unique 
        'odcls':"1,2,5,10", # unique 
        'ref_files': 'tmp_setup_files/Charger/'
    }, 
    'Clawclip': {
        # 'db_name': 'clawclip', # ALREADY IN PAGE  
        # 'app_name': 'Clawclip', # ALREADY IN PAGE 
        'species': '<i> Cute Beige Claw Clip </i>', # unique 
        'ref_genome':"/home/vandana/MGT-local/setup/example_inputs_2/genome.fasta", # unique 
        'lociloc':"/home/vandana/MGT-local/setup/example_inputs_2/lociLocationsInRef.txt", # unique
        'scheme_accessions':"/home/vandana/MGT-local/setup/example_inputs_2/Schemes", # unique 
        'schemeno':3, # unique 
        'odcls':"1,2,5,10", # unique 
        'ref_files': 'tmp_setup_files/Clawclip/'
    }
}