cut -f 1 popular-names.txt | sort | uniq -c | sort -k 1n
# 'cut -f 1 popular-names.txt'で名前のみ抜き出し
# ソートして重複をとる，-cで重複行数を表示
# 重複行数でソート