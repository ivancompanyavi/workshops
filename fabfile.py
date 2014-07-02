from fabric.api import run, task, sudo

@task
def post_run():
    sudo('apt-get update')
    sudo('apt-get install -y python-dev python-setuptools build-essential mysql-client mysql-server libmysqlclient-dev')
    sudo('easy_install pip')
    sudo('pip install Django mysql-python pillow')

