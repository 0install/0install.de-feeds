from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=PCC&type=release').read().decode('utf-8')
releases = [{'version': release['version'], 'major-version': release['majorVersion'], 'released': release['date']} for release in json.loads(data)['PCC'] if 'downloads' in release and release['version'].startswith('20')]
