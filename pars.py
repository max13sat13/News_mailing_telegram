""" Сделать из кода класс. 
Значения на входе: (канал, слова, поиск по этим словам или исключить)"""
from bs4 import BeautifulSoup
import requests as req
import pymorphy2
import string
import json
import lxml
import re
class ParserTelegramm():
	def __init__(self, link="https://t.me/s/agitblog", words=['мир'], choose=True, user_id=38):
		self.link = link
		self.words = words
		self.choose = choose
		self.times = []
		self.res = req.get(link)
		self.html = BeautifulSoup(self.res.text, 'lxml')
		self.titles = []
		self.count = 0
		self.list_all =[]
		self.outputs = []
		self.output_list = [] 
		self.news = {}
		self.user_id = user_id

	
	def get_data(self):
		start_list = []
		end_list = []
		for s in re.finditer('tgme_widget_message_owner_name', str(self.html)):
			start_list.append(s.end())
		for e in re.finditer(r'</time></a></span>', str(self.html)):
			end_list.append(e.start())
			elements = []
		for i in range(len(start_list)):
			elements.append(str(self.html)[start_list[i]: end_list[i]])


		for element in elements:
			href = re.findall(r'href="https://t\.me/\w+/\d+">', element)
			href = re.split(r'["]', str(href))
			text = re.findall(r'"\sdir="auto">.+', element)
			clean_text = re.split(r'[<>]', str(text))
			try:

				title_text = clean_text[1]
				href = href[1]

			except IndexError:
				title_text = ['пусто']
			else:
				self.news[href] = title_text.split()

	def print_list_all(self):
		print(self.list_all)

#часть вторая обработка списка
	def parser_text(self):
		"""форматирует текст, сохраняет его в best_format"""
		"""если список слов есть в словаре пользователя
		сохраняет ссылку в self.outputs"""
		morph = pymorphy2.MorphAnalyzer()

		for href, title in self.news.items():
			active = False
			list_format_words = []
			for word in title:
				format_word = word.strip().lower()
				best_format = format_word.rstrip(string.punctuation)
				normal_format = morph.parse(best_format)[0].normal_form
				list_format_words.append(normal_format)


#алгоритм если поиск по одному слову
			for word in self.words:
				word = word.lstrip()
				w = word.split(' ')
				if len(w) == 1:
					if word in list_format_words:
						active = True
					if word not in list_format_words:
						active = False

#алгоритм если несколько слов
				else:
					if w[0] in list_format_words:
						number = 0
						for f_word in list_format_words:
							number = number + 1

							if f_word == w[0]:
								count = len(w)
								for i in range(count):
									try:
										l_f_w = list_format_words[number-1+i]
									except IndexError:
										break
									else:
										if w[i] == l_f_w:
											if i == count-1:
												active = True
										else:
											break
#флаги отвечают за поиск по словам или всё кроме слов"
			if self.choose == False:
				if active == False:
					self.outputs.append(href)
			if self.choose == True:
				if active == True:
					self.outputs.append(href)

					
	def output(self):
		for self.output in set(self.outputs):
				print(self.output)
				
				
				 
	def print_all(self):
		for href, title in self.news:
			print(href + ' ' + title)

#часть третья подготовка в выводу и вывод

	def uniq_message(self):
		"""открывает json файл, если его нет, сохраняет
		self.output в нём.
		Если есть перебирает ссылки из self.output
		в last_list.  Если ссылка уникальна сохраняет её
		в self_output_list. А потом сохраняет эту ссылку в 
		файле last_list
		"""
		file_name = 'last_list.json'
		self.uniq_list = {}
		self.first_outputs = []
		for i in set(self.outputs):
			self.first_outputs.append(i)
			
		
		try:
			with open(file_name) as f_obj:
				last_list = json.load(f_obj)
		except FileNotFoundError:
			with open(file_name, 'w') as file_object:
				
				self.uniq_list = {self.user_id : self.first_outputs}
				json.dump(self.uniq_list, file_object)
			for set_new in self.first_outputs:
				self.output_list.append(set_new)		
		else:
			for set_new in self.first_outputs:
				if str(self.user_id) in last_list.keys():
					for user_id, list_url in last_list.items():

						if str(self.user_id) == str(user_id):
							if set_new not in list_url:
								self.output_list.append(set_new)
				else:
					last_list[self.user_id] = []
					with open(file_name, 'w') as file_object:
						json.dump(last_list, file_object)

			if self.output_list:
				for url in self.output_list:
					last_list[self.user_id].append(url)
				with open(file_name, 'w') as file_object:
					json.dump(last_list, file_object)


	def output_telegram(self):
		"""
		следит чтобы ссылки были в одном экземпляре
		и возращает их в функцию
		"""
		messages = []
		for message in self.output_list:
			messages.append(message)
		return (set(messages))
		
	def output_test(self):
		for message in set(self.output_list):
			print("final" + message)
			
def test():
	test = ParserTelegramm()
	test.get_data()
	test.print_list_all()
	test.print_list_all()
	test.parser_text()
	test.output()
	test.uniq_message()
	test.output_telegram()



def start():
	test = ParserTelegramm()
	test.get_data()
	test.parser_text()
	test.uniq_message()
	return test.output_telegram()



