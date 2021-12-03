input = 'inputs/day1_input.txt'
with open(input) as f:
    text = f.readlines()
int_list = list(map(int, text))

# puzzle one
increase_list = []
for i in range(len(int_list)):
    if i == 0:
        continue # skip the first one
    j = i - 1
    if int_list[i] > int_list[j]:
        increase_list.append(True)
    else:
        increase_list.append(False)
print(sum(increase_list))

# puzzle two
window_list = []
for i in range(len(int_list)):
    if i <2:
        continue # skip the first two
    h = i - 2
    j = i - 1
    my_sum = int_list[i] + int_list[j] + int_list[h]
    window_list.append(my_sum)
window_increases = []
for i in range(len(window_list)):
    if i == 0:
        continue # skip the first one
    j = i - 1
    if window_list[i] > window_list[j]:
        window_increases.append(True)
    else:
        window_increases.append(False)
print(sum(window_increases))