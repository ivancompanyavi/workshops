from fabric.api import task, sudo, env

@task
def vagrant(name=''):
    """
    optional command `fab vagrant <something>`
    sets the public key for root and then switches to the root user
    """
    from fabtools import vagrant as _vagrant
    _vagrant.vagrant(name)
    env['host_string'] = env['host_string'].replace('vagrant', 'root')

@task
def install():
    sudo('apt-get update')
    sudo('apt-get install -y python-dev python-setuptools build-essential mysql-client mysql-server libmysqlclient-dev libjpeg-dev zlib1g-dev libpng12-dev')
    sudo('easy_install pip')
    sudo('pip install Django mysql-python south')
    sudo('ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib')
    sudo('ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib')
    sudo('ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib')
    sudo('pip install pillow')
    sudo('gem update --system')
    sudo('gem install compass')