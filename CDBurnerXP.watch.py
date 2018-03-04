from urllib import request
import re

data = request.urlopen('http://download.cdburnerxp.se/portable/').read().decode('utf-8')
matches = re.findall(r'CDBurnerXP-x64-([0-9\.]+).zip</a>\s*(....-..-..)', data)
releases = [{'version': match[0], 'released': match[1]} for match in matches if match[0][0:4] != '3.0.']
