from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=GO&type=release').read().decode('utf-8')
releases = [{
    'version': release['version'],
    'major-version': release['majorVersion'],
    'released': release['date']
} for release in json.loads(data)['GO'] if 'downloads' in release and not release['version'].startswith('2017') and not release['version'].startswith('2018')]
