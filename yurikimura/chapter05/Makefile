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

answer:
	python knock40.py > 40.txt
	python knock41.py > 41.txt
	python knock42.py > 42.txt
	python knock43.py > 43.txt
	python knock44.py
	python knock45.py > 45.txt
	python knock46.py > 46.txt
	python knock47.py > 47.txt
	python knock48.py > 48.txt
	python knock49.py > 49.txt

clean:
	rm -rf output44*
	rm -rf 4*
