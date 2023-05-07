
from amdm import AmDm
import json
import re
from bs4 import BeautifulSoup

q = 'qq'

chords = AmDm.get_chords_list('', q)
url = chords[0]["url"]
url = url[url.index(":") + 1:]
song = AmDm.get_chords_song('', url)
list_of_song = [x for x in song.split('\n\n')]
with open("song.html", "w", encoding="cp1251") as s:
    s.write(song)
clean_text = BeautifulSoup(song, "lxml").text

for x in list_of_song:
    if len(x) < 400:
        print(x, '|')
    else:
        print('LOOOOOONG', len(x))
        break
print(song.index('\n'), song.encode('unicode_escape'))