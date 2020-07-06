import datetime



def logger(path='default_log.txt'):
	def _logger(old_foo):
		def new_foo(*args, **kwargs):
			result = old_foo(*args, **kwargs)

			output = f'''
	Вызвана функция {old_foo.__name__}
	C аргументами {args} {kwargs}
	Время вызова функции - {datetime.datetime.utcnow()}

	------------------------------------------------------'''
			print(output)

			with open(path, 'a', encoding='utf-8') as file:
				file.write(output)

			return result

		return new_foo

	return _logger
