import re
import urllib
from zipfile import ZipFile

from django.core.management.base import BaseCommand
from django.conf import settings

import whois
from djangoproject.domains.models import DomainName

SHITTY_TLDS = ['biz', 'info']
UNKNOWN_TLDS = ['ca', 'us']

class Command(BaseCommand):

    def handle(self, *args, **options):
        #urllib.urlretrieve(settings.DROPLIST_URL, settings.DROPLIST_LOCAL_CACHE_FILE)
        zip = ZipFile(settings.DROPLIST_LOCAL_CACHE_FILE, 'r')
        filenames = zip.namelist()
        for filename in filenames:
            file = zip.open(filename)
            while True:
                line = file.readline()
                if not line:
                    break
                domain = [x.strip() for x in line.split(',')][0]

                if domain.split('.').pop() not in SHITTY_TLDS + UNKNOWN_TLDS:
                    try:
                        if not '-' in domain and \
                           not DomainName.objects.filter(name=domain).exists() and \
                           not bool(re.search('[0-9]', domain)):
                            result = whois.query( domain )
                            DomainName.objects.get_or_create(**result.__dict__)
                            print domain
                        else:
                            print 'x: ' + domain
                    except:
                        pass

