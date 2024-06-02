from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=GO&type=release').read().decode('utf-8')
releases = [{
    'version': release['version'],
    'released': release['date']
} for release in json.loads(data)['GO'] if 'downloads' in release and 'linuxARM64' in release['downloads']]
