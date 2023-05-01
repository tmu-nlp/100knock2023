read N
lines=`cat popular-names.txt | wc -l`
# '|'で左のコマンドの実行結果を標準入力として右のコマンドに与える．
# `wc -l popular-names.txt`だとファイル名も一緒に出力されてしまうので，その回避のため．
# hoge='command'で，commandの実行結果がhogeに代入される．
child_lines=$(($lines/$N))
split -l $child_lines popular-names.txt k16_out/k16_sh_
# lines%N!=0のとき，余りに相当する行数分だけ新たにファイルができてしまい，N+1個に分割されてしまう．悲しい…