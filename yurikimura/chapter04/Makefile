dataset:
	curl https://nlp100.github.io/data/neko.txt > neko.txt

mecab:
	brew install mecab-ipadic
	brew install mecab
	mecab neko.txt -o neko.txt.mecab

clean:
	rm *.txt
