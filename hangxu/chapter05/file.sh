#cabocha: error while loading shared libraries: libcabocha.so.5: cannot open shared object file: No such file or directory
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
echo $LD_LIBRARY_PATH

cabocha -f1 -o ai.ja.txt.parsed ai.ja.txt