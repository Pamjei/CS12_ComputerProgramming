n = int(input())
output = []
for i in range(n):
    low = int(input())
    med = int(input())
    goal = int(input())
    for x in range(1,med+1):
        left = goal - (5*x)
        if left < 1:
            break
    if left == 1 and med == 1: #special case na walang kwenta si med
        output.append(goal/2)
    elif left < 0 and med < goal:
        left = left + 10
        output.append(left/2)
    elif left%2 == 0:
        output.append(left/2)
    elif left %2 != 0 and med > 1: #sobra ng meds
        left = left + 5
        output.append(left/2)
    else:
        output.append(-1)
for i in range(len(output)):
    print (int(output[i]))
