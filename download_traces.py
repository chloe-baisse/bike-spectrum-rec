import requests
import tarfile
from tqdm import tqdm

def download_file(url, filename=''):
	print("Starting extraction")
	try:
		req = requests.get(url, stream=True)
		total = int(req.headers.get('content-length', 0))
		with open(filename, 'wb') as f:
			tqdm_params = {'desc': filename,
                'total': total,
                'miniters': 1,
                'unit': 'B',
                'unit_scale': True,
                'unit_divisor': 1024}
			with tqdm(**tqdm_params) as pb:
				for chunk in req.iter_content(chunk_size=8192):
					if chunk:
						pb.update(len(chunk))
						f.write(chunk)
			return filename
	except Exception as e:
		print(e)
		return

def extract(archive, dest):
	with tarfile.open(archive) as tar:
		tar.extractall(dest, filter='data')
	print("Extraction completed")


url_training = "https://zenodo.org/records/18267783/files/training_traces.tar.xz?download=1"
url_testing = "https://zenodo.org/records/18267783/files/testing_traces.tar.xz?download=1"
filename_training = "data/training_traces.tar.xz"
filename_testing = "data/testing_traces.tar.xz"

download_file(url_training, filename_training)
extract(filename_training,"data/")

download_file(url_testing, filename_testing)
extract(filename_testing,"data/")



