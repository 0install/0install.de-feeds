from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=RD&type=release').read().decode('utf-8')
releases = [{'version': release['version'], 'download-url': release['downloads']['zip']['link'], 'major-version': release['majorVersion'], 'released': release['date']} for release in json.loads(data)['RD'] if 'downloads' in release]
