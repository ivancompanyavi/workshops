#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from fabric.api import cd, sudo, run, put, task, env, settings
import pkg_resources


def config_file(folder, filepath):
    return pkg_resources.resource_filename(__name__,
                                           '/config/{0}/{1}'.format(folder, filepath))

@task
def vagrant(name=''):
    """
    optional command `fab vagrant <something>`
    sets the public key for root and then switches to the root user
    """
    from fabtools import vagrant as _vagrant
    _vagrant.vagrant(name)
    env['host_string'] = env['host_string'].replace('vagrant', 'root')


def command_exists(command):
    """
    Checks if the command 'command' exists
    """
    result = False
    with settings(warn_only=True):
        checked = run('command -v %s' % command)
        if checked.return_code == 0:
            result = True

    return result


def install_wget():
    if not command_exists('wget'):
        sudo('yum install -y wget')


def _install_python():
    install_wget()
    if not command_exists('python2.7'):
        run('mkdir -p /home/vagrant/src')
        with cd('/home/vagrant/src'):
            run('wget --no-check-certificate https://www.python.org/ftp/python/2.7.7/Python-2.7.7.tar.xz')
            run('tar xf Python-2.7.7.tar.xz')
        with cd('/home/vagrant/src/Python-2.7.7'):
            sudo('./configure --prefix=/usr')
            sudo('make && make altinstall')
        with cd('/home/vagrant'):
            run('echo "alias python=/usr/bin/python2.7" >> .bashrc')
            run('source .bashrc')


def _install_pip():
    run('mkdir -p /home/vagrant/src')
    _install_python()
    install_wget()
    if not command_exists('pip'):
        with cd('/home/vagrant/src'):
            run('wget https://bootstrap.pypa.io/ez_setup.py')
            sudo('/usr/bin/python2.7 ez_setup.py')
            run('wget https://bootstrap.pypa.io/get-pip.py')
            sudo('/usr/bin/python2.7 get-pip.py')


def _install_nginx():
    put(config_file('nginx', 'nginx.repo'), '/etc/yum.repos.d/', use_sudo=True)
    sudo('yum install -y nginx')

    put(config_file('nginx', 'nginx.conf'), '/etc/nginx/', use_sudo=True)

    sudo('mkdir -p /etc/supervisor/conf.d/')
    sudo('mkdir -p /var/log/uwsgi')
    sudo('chmod 777 -R /var/log/uwsgi')
    sudo('chown -R vagrant: /var/log/uwsgi')
    put(config_file('supervisor', 'supervisord.conf'), '/etc/supervisord.conf', use_sudo=True)
    put(config_file('supervisor', 'uwsgi.conf'), '/etc/supervisor/conf.d/', use_sudo=True)


def _install_bower():
    #first, we have to install Node
    with cd('/home/vagrant/src'):
        run('wget http://nodejs.org/dist/v0.10.31/node-v0.10.31.tar.gz')
        run('tar zxf node-v0.10.31.tar.gz')
        with cd('node-v0.10.31'):
            run('sudo su -')
            run('./configure')
            run('make')
            sudo('make install')
    run('npm install -g bower')

@task
def install():
    sudo('yum install -y zlib-devel bzip2-devel openssl-devel curses-devel bzip2-devel sqlite-devel mysql-server mysql-devel python-devel ruby ruby-devel rubygems node npm')
    sudo('npm install -g bower')
    _install_pip()
    with cd('/vagrant'):
        sudo('pip install -r requeriments.txt')
    _install_nginx()
    #_install_bower()
    sudo('gem update --system')
    sudo('gem install compass')
    with cd('/vagrant/'):
        run('bower install')
    run('supervisord')
    run('supervisorctl update && supervisorctl restart all')
    sudo('service mysqld start')


@task
def up():
    sudo('nginx')
