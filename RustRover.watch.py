from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=RR&type=release').read().decode('utf-8')
releases = [{
    'version': release['version'],
    'released': release['date']
} for release in json.loads(data)['RR'] if 'downloads' in release and 'windowsZip' in release['downloads']]
