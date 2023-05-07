import re
string = re.split(r'\b', 'Words\n\n, words\n, words.')

print(string)
# song = open('song.html', encoding='cp1251').read()
#
# list_of_song = [x for x in song.split('\n\n')]
# # with open("song.html", "w", encoding="cp1251") as s:
# #     s.write(song)
# # clean_text = BeautifulSoup(song, "lxml").text
#
# for x in list_of_song:
#     print(x, '\n|||\n')
#
# print(list_of_song)
