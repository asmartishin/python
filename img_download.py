import requests
from StringIO import StringIO
from PIL import Image
import profile

image_name = 'test.jpg'
url = 'http://vivaset.ru/assets/images/products/1210/520x520/1ecb80e04779f8a46f04b6afcca0d6a6.jpg'
r = requests.get(url)
i = Image.open(StringIO(r.content))
i.save(image_name)
