import random

picknum = int(input("How many line of quick picks do you want? : "))
for i in range(picknum):
    data = []
    for i in range(6):
        while True:
            pick = random.randint(1,45)
            if pick in data:
                continue
            else:
                data.append(pick)
            break
    data.sort()
    print("{:3d},{:3d},{:3d},{:3d},{:3d},{:3d}".format(data[0],data[1],data[2],data[3],data[4],data[5]))