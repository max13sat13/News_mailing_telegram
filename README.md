#Бот для парсинга и рассылки постов в телеграмме.
Алгоритм работы: 
-Запрашивает у пользователя критерии по которым будут парсится посты в телеграм.(канал, список слов, поиск по словам или всё кроме указанных слов)
-Парсит посты в телеграмме на наличие в них запрашиваемых пользователем слов.
-Отправляет посты пользователю в реальном времени.
Назначение скриптов:
fsm_config.py содержит настройки для бота
pars.py - парсит посты в телеграм
task.py - отправляет посты пользователю
handlers.py собирает данные пользователя
help.py раздел помощи
delete.py удаляет канал
main.py запускает бота
Протестировать бота можно по адресу: https://t.me/WatherNewsBot 

# News_mailing_telegram
Parsing posts in Telegrams, and mailing to subscribers.
Algorithm of operation:
-Requests from the user the criteria by which posts in Telegram will be parsed.(channel, word list, word search, or all but the specified words)
-Parses the posts in the telegram for the presence of the words requested by the user in them.
-Sends posts to the user in real time.
Purpose of scripts:
fsm_config.py contains settings for the bot
pars.py - parses posts in Telegram
task.py - sends posts to the user
handlers.py collects
help user data.py help
section delete.py deletes
the main channel.py launches a bot
You can test the bot at: https://t.me/WatherNewsBot

