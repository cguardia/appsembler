import json

from paste import httpserver
from paste.deploy import loadapp

CONFIG = """[DEFAULT]
var = %%(here)s/../var

[instance:pg]
dsn = dbname='%(name)s' user='%(user)s' host='%(host)s' password='%(password)s'
repozitory_db_string = postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(name)s
"""

def setup_instances():
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    cred = vcap_services.values()[0][0]['credentials']

    instances = CONFIG % cred

    instances_file = open('./etc/instances.ini','w')
    instances_file.write(instances)
    instances_file.close()

if __name__ == '__main__':
    setup_instances()
    port = int(os.getenv('VCAP_APP_PORT', '8000'))
    host = os.getenv('VCAP_APP_HOST', '0.0.0.0')
    httpserver.serve(loadapp('config:karlserve.ini', relative_to='./etc'),
                     host=host, port=port)
