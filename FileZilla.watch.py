from urllib import request
import re

data = request.urlopen('https://sourceforge.net/projects/filezilla/files/FileZilla_Client/').read()
matches = re.findall(r'([0-9\.]+)</a></th>\n\s*<td headers="files_date_h" class="opt"><abbr title="(....-..-..)', data.decode())
releases = [{'version': match[0], 'released': match[1]} for match in matches if match[0][0:4] != '3.0.']
