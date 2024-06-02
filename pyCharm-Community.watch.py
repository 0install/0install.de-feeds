from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=PCC&type=release').read().decode('utf-8')
releases = [{
    'version': release['version'],
    'released': release['date']
} for release in json.loads(data)['PCC'] if 'downloads' in release and 'windowsZipARM64' in release['downloads']]
