input = 'inputs/day2_input.txt'
with open(input) as f:
    text = f.readlines()

dirList = []
amtList = []
for i in text:
    some_var = i.split(' ')
    dirList.append(some_var[0])
    amtList.append(int(some_var[1]))

def nav(start=(0, 0), input='down', amount=1):
    # returns the difference between a starting point and the directions supplied
    if input == 'forward':
        end = (start[0] + amount, start[1])
    elif input == 'down':
        end = (start[0], start[1] + amount)
    elif input == 'up':
        end = (start[0], start[1] - amount)
    return(end)

print(nav((0, 0), dirList[9], amtList[9]))

# I just keep adding everything to 0,0
# It's probably really simple but I can't wrap my head around updating the location