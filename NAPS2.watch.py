from urllib import request
import json

data = request.urlopen('https://api.github.com/repos/cyanfish/naps2/releases').read().decode('utf-8')
releases = [{'version': release['name'], 'released': release['published_at'][0:10]} for release in json.loads(data) if release['assets'] and 'b' not in release['name']]
