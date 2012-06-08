import os

def setup_instance():
    port = os.getenv('VCAP_APP_PORT', '8080')
    host = os.getenv('VCAP_APP_HOST', '0.0.0.0')

    instances_file = open('parts/instance/etc/zope.conf')
    instances_file_content = instances_file.read().replace('PLONE_HTTP_PORT', port)
    instances_file.close()
    
    new_instances_file = open('parts/instance/etc/zope.conf', 'w')
    new_instances_file.write(instances_file_content)
    new_instances_file.close()

if __name__ == '__main__':
    setup_instance()
    os.execl('bin/instance', 'instance', 'fg')
