from fabric.api import local

def up():
    local('jekyll --server --auto')

def deploy():
    local('jekyll')
    local('scp -r _site/* nimbus:octave')
