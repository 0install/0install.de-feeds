from urllib import request
import json

def convert(release):
    original_version = release['tag_name'].strip('v')
    if 'RC' in original_version:
        build_version = original_version
        version = original_version.replace('.RC', '-rc').replace('RC', '-rc')
        stability = 'testing'
    else:
        build_version = original_version if original_version.count('.') > 1 else original_version + '.00'
        version = original_version.replace('.0', '.')
        stability = 'stable'
    released = release['published_at'][0:10]
    return {'version': version, 'original-version': original_version, 'build-version': build_version, 'stability': 'stability', 'released': released}

data = request.urlopen('https://api.github.com/repos/gitextensions/gitextensions/releases').read().decode('utf-8')
releases = [convert(release) for release in json.loads(data) if len(release['assets']) > 0]
