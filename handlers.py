from telebot import types

from loader import bot, news
from utils import get_lang, send_page
import logging
import random

logger = logging.getLogger(__name__)

@bot.message_handler(commands=['start', "help"])
def start_cmd(msg: types.Message):
	bot.reply_to(msg, "hi i am a bot for searching news\ncommands:\n/top request text(optional) - get random news from the top\n/sources - get all sources\nany word - get any news\n\nbot worked in eng/rus languages, to search for articles in one of these languages, just start typing your query in that language")
	

@bot.message_handler(commands=["top"])
def get_top(msg: types.Message):
	args = msg.text.split(' ', 1)
	if len(args)>1:
		q = args[1]
		lang = get_lang(q)
	else:
		q = None
		lang = "en"
	page_json=news.get_top_headlines(q=q, language=lang)
	send_page(bot, page_json, msg)

		
@bot.message_handler(commands=["sources", "src"])
def sources(msg: types.Message):
	sources_json = news.get_sources().get("sources")
	sources = map(lambda s: s["url"], sources_json)
	text = "\n".join(sources)
	bot.reply_to(msg, text, parse_mode="Markdown")
	

@bot.message_handler()
def find_page(msg: types.Message):
	
	lang = get_lang(msg.text)
	page_json = news.get_everything(q=msg.text, language=lang)
	send_page(bot, page_json, msg)
