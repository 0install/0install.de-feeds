from urllib import request
import json
import re

def handle(version):
    linux64url = request.urlopen('https://vscode-update.azurewebsites.net/' + version + '/linux-x64/stable').url
    linux32url = request.urlopen('https://vscode-update.azurewebsites.net/' + version + '/linux-ia32/stable').url
    return {
        'version': version,
        'release-id': re.search('stable/([0-9a-f]+)/code', linux64url).group(1),
        'linux-amd64-timestamp': re.search('-([0-9]+)_amd64', linux64url).group(1),
        'linux-i386-timestamp': re.search('-([0-9]+)_i386', linux32url).group(1)
    }

data = request.urlopen('https://api.github.com/repos/Microsoft/vscode/tags').read().decode('utf-8')
releases = [handle(tag['name']) for tag in json.loads(data) if not '/' in tag['name']]
