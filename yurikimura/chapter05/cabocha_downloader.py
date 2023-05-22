# CRF++のソースファイルのダウンロード
import gdown

url = "https://drive.google.com/uc?id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ"
output = "crfpp.tar.gz"
gdown.download(url, output, quiet=False)

# CaboChaのソースファイルのダウンロード
url = "https://drive.google.com/uc?id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU"
output = "cabocha-0.69.tar.bz2"
gdown.download(url, output, quiet=False)
