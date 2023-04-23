def is_skip(letter):
    skip_list = [" ", ",", "."]
    for i in skip_list:
        if letter == i:
            return True
    return False

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
cnt = 0
cnt_list = []
for i in s:
    if is_skip(i) == True:
        if cnt == 0:
            continue
        cnt_list.append(cnt)
        cnt = 0
        continue
    else:
        cnt += 1

print(cnt_list)