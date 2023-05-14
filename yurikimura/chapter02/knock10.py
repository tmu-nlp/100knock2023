# 10. 行数のカウントPermalink
# 行数をカウントせよ．確認にはwcコマンドを用いよ

with open('popular-names.txt', 'r') as f:
    lines = f.readlines()

print(len(lines))
