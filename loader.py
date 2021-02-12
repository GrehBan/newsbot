from telebot import TeleBot
from newsapi import NewsApiClient

import logging
from constants import TOKEN, API_KEY

bot = TeleBot(TOKEN)
news = NewsApiClient(API_KEY)

logging.basicConfig(filename='log.log', level=logging.INFO)