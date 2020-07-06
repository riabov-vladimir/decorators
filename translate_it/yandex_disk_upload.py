import requests


def upload_to_ya_disk(output_file_path):

	TOKEN = 'AgAAAAAd7LCoAADLW7cgFmFB3Uqtuquv3tektMM'

	PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

	headers = {'Accept': 'application/json', 'Authorization': TOKEN}

	params = {'path': '/translate/{}'.format(output_file_path), 'overwrite': True}


	response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
	json_ = response.json()

	upload_link = ''.join(json_['href'])

	files={'file': open(output_file_path,'rb')}
	response = requests.put(upload_link, files=files)
	print('Запись на Яндекс Диск завершилась с кодом', response.status_code)
