from urllib import request
import json

data = request.urlopen('https://data.services.jetbrains.com/products/releases?code=RD&type=release').read().decode('utf-8')
releases = [{
    'version': release['version'],
    'released': release['date'],
    'download-url-windows': release['downloads']['zip']['link'],
    'download-url-linux': release['downloads']['linux']['link']
} for release in json.loads(data)['RD'] if 'downloads' in release]
