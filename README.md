# newsbot
@NewsThreadBot - it is a simple bot for viewing news, in two languages (en/ru)
based on [pytelegrambotapi](https://github.com/eternnoir/pyTelegramBotAPI) and [newsapi](newsapi.org)

### Using
```bash
git clone https://github.com/GrehBan/newsbot.git
cd newsbot
pip install -r requirements.txt
nano .env
```

write in .env this:
    TOKEN=YOUR_TELEGRAM_TOKEN
    API_KEY=YOUR_NEWSAPI_KEY

```bash
python main.py
```
