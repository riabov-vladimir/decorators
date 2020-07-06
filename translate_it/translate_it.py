import requests
import os
import datetime
from yandex_disk_upload import upload_to_ya_disk
from logger_deco import logger

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


@logger('translations_log.txt')
def translate_it(text, from_lang=None, to_lang='ru', input_file_path=None, output_file_path='default_translate_log.txt'):
    """
    ПОРЯДОК ПЕРЕДАЧИ АРГУМЕНТОВ:
    1* - ручной ввод текста для перевода (если переводим из файла, текст из файла заменит это поле, так что
    можно оставить заглушку)
    2* - язык с которого переводим
    3 - язык на который переводим (по умолчанию русский)
    4 - файл из которого берём текст для перевода (по умолчанию None)
    5 - файл в который сохраняется перевод (по умолчанию используется default_translate_log.txt в который я обычно
    логирую все переводы с временем и датой)
    _________________________________________
    * - обязательные к передаче аргументы
    """

    if input_file_path is not None:
        with open(input_file_path, 'r', encoding='utf-8') as input_text:
            text = input_text.read()


    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{0}-{1}'.format(from_lang, to_lang),
        # если в поле lang оставить только переменную to_lang, можно будет не указывать исходный язык и тогда
        # можно было бы пользоваться функцией в упрощенном варианте, передавая ей только текст, а она бы переводила
        # его на русский.
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        output_file.write(os.linesep)
        output_file.write(str(datetime.datetime.utcnow()))
        output_file.write(os.linesep)
        if input_file_path is not None:
            output_file.write(f'{input_file_path} {from_lang} -> {to_lang}: ')
            output_file.write(''.join(json_['text']))
        else:
            output_file.write(f'{text} {from_lang} -> {to_lang} ')
            output_file.write(''.join(json_['text']))

    upload_to_ya_disk(output_file_path)

    return ''.join(json_['text'])
