import re
from telebot import types
import random


def get_lang(text: str):
	is_rus = re.findall(r'[а-яА-Я]+', text)
	if is_rus:
		return "ru"
	return "en"


def send_page(bot, page_json, msg):
	articles = page_json.get("articles")
	if not articles:
		bot.reply_to(msg, "Nothing found")
		return
	article = random.choice(articles)
	kb = types.InlineKeyboardMarkup()
	kb.add(types.InlineKeyboardButton(text="Read more", url=article["url"]))
	bot.send_photo(chat_id=msg.chat.id, photo=article["urlToImage"], caption=article["title"], reply_markup=kb)