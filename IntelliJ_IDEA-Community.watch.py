from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=IIC&type=release').read().decode('utf-8')
releases = [{
    'version': release['version'],
    'build': release['build'],
    'released': release['date']
} for release in json.loads(data)['IIC'] if 'downloads' in release and 'linuxARM64' in release['downloads']]
