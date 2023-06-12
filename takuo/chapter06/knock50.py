import re
import os
import random

with open(f"{os.path.dirname(__file__)}/NewsAggregatorDataset/newsCorpora.csv", 'r') as rawfile:
    publishers = ["Reuters", "Huffington Post",
                  "Businessweek", "Contactmusic.com", "Daily Mail"]
    data_from_publs = []

    line = rawfile.readline()
    while (line != ""):  # 一行づつよんでく
        line_items = line.split('\t')
        if (line_items[3] in publishers):
            data_from_publs.append(line_items)  # 対象publisherならリストに追加
        line = rawfile.readline()

    random.shuffle(data_from_publs)

    data_total = len(data_from_publs)
    valid_data = data_from_publs[:data_total//10]  # 10%
    test_data = data_from_publs[data_total//10:data_total//10*2]  # 10%
    train_data = data_from_publs[data_total//10*2:]  # others

    with open(f"{os.path.dirname(__file__)}/train.txt", 'w') as out_train:
        for data in train_data:
            out_train.write(f"{data[4]}\t{data[1]}\n")

    with open(f"{os.path.dirname(__file__)}/valid.txt", 'w') as out_valid:
        for data in valid_data:
            out_valid.write(f"{data[4]}\t{data[1]}\n")

    with open(f"{os.path.dirname(__file__)}/test.txt", 'w') as out_test:
        for data in test_data:
            out_test.write(f"{data[4]}\t{data[1]}\n")
