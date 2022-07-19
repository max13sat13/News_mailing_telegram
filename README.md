# Бот для парсинга и рассылки постов в телеграмме.
Алгоритм работы:
<br>-Запрашивает у пользователя критерии по которым будут парсится посты в телеграм.(канал, список слов, поиск по словам или всё кроме указанных слов)
<br>-Парсит посты в телеграмме на наличие в них запрашиваемых пользователем слов.
<br>-Отправляет посты пользователю в реальном времени.
<br>Назначение скриптов:
<br>fsm_config.py содержит настройки для бота
<br>pars.py - парсит посты в телеграм
<br>task.py - отправляет посты пользователю
<br>handlers.py собирает данные пользователя
<br>help.py раздел помощи
<br>delete.py удаляет канал
<br>main.py запускает бота
<br>Протестировать бота можно по адресу: https://t.me/WatherNewsBot 

# News_mailing_telegram
Parsing posts in Telegrams, and mailing to subscribers.
<br>Algorithm of operation:
<br>-Requests from the user the criteria by which posts in Telegram will be parsed.(channel, word list, word search, or all but the specified words)
<br>-Parses the posts in the telegram for the presence of the words requested by the user in them.
<br>-Sends posts to the user in real time.
<br>Purpose of scripts:
<br>fsm_config.py contains settings for the bot
<br>pars.py - parses posts in Telegram
<br>task.py - sends posts to the user
<br>handlers.py collects
<br>help user data.py help
<br>section delete.py deletes
<br>the main channel.py launches a bot
<br>You can test the bot at: https://t.me/WatherNewsBot
