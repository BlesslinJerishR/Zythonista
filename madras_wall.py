wall = 88
climb = 12
fall = 8
gain = climb - fall
steps = 0
trying = True
arrear = 0
while True:
    # print(steps)
    arrear += 1
    if steps >= 88 or steps + 12 >= 88:
        trying = False
        break
    steps += gain
print(arrear)  