import os

import json

from paste import httpserver
from paste.deploy import loadapp

CONFIG = """
dsn = dbname='%(name)s' user='%(user)s' host='%(host)s' password='%(password)s'
"""

def setup_dbconfig():
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    cred = vcap_services.values()[0][0]['credentials']

    dbconfig = CONFIG % cred

    # To do: find the best place to put this
    dbconfig_file = open('./parts/relstorage?','w')
    dbconfig_file.write(dbconfig)
    dbconfig_file.close()

if __name__ == '__main__':
    setup_dbconfig()
    os.execv('./bin/client1', ('fg',))
