from fabric.api import local

def up():
    local('jekyll serve --watch')

def deploy():
    local('jekyll')
    local('scp -r _site/* nimbus:octave')
