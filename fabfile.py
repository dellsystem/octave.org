from fabric.api import local

def up():
    local('jekyll --server --auto')
