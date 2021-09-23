######### TEST 1 - Use Pyshorteners #######

import pyshorteners as sh

link = 'https://github.com/PaulCollas/hi-python/blob/main/README.md'

s = sh.Shortener()

print(s.tinyurl.short(link))

