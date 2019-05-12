from urllib import request
import re

data = request.urlopen('https://www.autoitscript.com/autoit3/files/archive/autoit/').read().decode('utf-8')
matches = re.findall(r'autoit-v([0-9\.]+).zip<\/a>\s*(....-..-..)', data)
releases = [{'version': match[0], 'released': match[1]} for match in matches]
