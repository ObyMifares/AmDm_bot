import telebot
from amdm import AmDm
import json
from bs4 import BeautifulSoup

tk = open("tk.json")
tk = json.load(tk)["TOKEN"]
bot = telebot.TeleBot(tk)


@bot.message_handler(commands=['start'])
def start_answer(message):
    bot.send_message(message.chat.id, 'напиши /song и запрос назвиние песни с автором или слова')


@bot.message_handler(commands=['song'])
def send_song(message):

    name_of_song = message.text
    name_of_song = name_of_song[6:]
    bot.send_message(message.chat.id, name_of_song)
    try:
        chords = AmDm.get_chords_list('', name_of_song)
        url = chords[0]["url"]
        url = url[url.index(":") + 1:]
        song = AmDm.get_chords_song('', url)
        song = song.replace('\n\n', 'THISISNOTASONG')
        song = song.replace('\n \n', 'THISISNOTASONG')
        song = song.replace('\n\r\n', 'THISISNOTASONG')
        song = song.replace('\n\t\n', 'THISISNOTASONG')
        song = song.replace('\n\b\n', 'THISISNOTASONG')
        list_of_song = [x for x in song.split('THISISNOTASONG')]

        for x in list_of_song:
            clean_text = BeautifulSoup(x, "lxml").text
            bot.send_message(message.chat.id, clean_text,)
                             #parse_mode='html'
    except Exception as ex:
        bot.send_message(message.chat.id, f'ниче не нашел{ex}')



def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()