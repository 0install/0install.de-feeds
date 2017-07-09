from urllib import request
import json

def convert(release):
    version_tag = release['tag_name'].strip('v')
    if 'RC' in version_tag:
        version_build = version_tag
        version = version_tag.replace('RC', '-pre')
    else:
        version_build = version_tag if version_tag.count('.') > 1 else version_tag + '.00'
        version = version_tag.replace('.0', '.')
    released = release['published_at'][0:10]
    return {'version': version, 'version-tag': version_tag, 'version-build': version_build, 'released': released}

data = request.urlopen(request.Request('https://api.github.com/repos/gitextensions/gitextensions/releases')).read()
releases = [convert(release) for release in json.loads(data) if len(release['assets']) > 0]
