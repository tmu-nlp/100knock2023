dataset:
	wget https://nlp100.github.io/data/ai.ja.zip
	unzip ai.ja.zip
	rm ai.ja.zip*

cabocha:
	make dataset
	pip install gdown
	python cabocha_downloader.py
	tar xvf crfpp.tar.gz
	tar -xvf cabocha-0.69.tar.bz2
	cabocha -f1 -o ai.ja.txt.parsed ai.ja.txt
	rm crfpp.tar.gz*
	rm -rf cabocha-*
	rm -rf CRF++*
	pip uninstall gdown
