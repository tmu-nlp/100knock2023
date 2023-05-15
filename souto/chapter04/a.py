import MeCab

tagger = MeCab.Tagger('-d /opt/homebrew/lib/mecab/dic/ipadic')


print(tagger.parse("おいしいです"))