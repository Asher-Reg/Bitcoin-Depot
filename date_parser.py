import calendar
import csv

def intervening_days(day1, day2):
    weektest = list(calendar.day_name)*2
    d1 = weektest.index(day1)
    d2 = weektest.index(day2,d1+1)
    return weektest[d1:d2+1]

print(intervening_days("Monday","Sunday"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


with open('hours_final.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

newlist = []
f = open("ex.txt", "w")

k = 0
print(len(data))
while k < len(data):
    print(k)
    print(data[k])
    if len(data[k]) == 0:
        # newlist.append('24/7, 24/7, 24/7, 24/7, 24/7, 24/7, 24/7')
        f.write('error\n')
        k+=1
        continue
    if data[k][0] == '24/7':
        # newlist.append('24/7, 24/7, 24/7, 24/7, 24/7, 24/7, 24/7')
        f.write('24/7, 24/7, 24/7, 24/7, 24/7, 24/7, 24/7\n')
        k+=1
        continue
    a = 0
    while a < len(data[k]):
        try:
            z = len(intervening_days(data[k][a],data[k][a+1]))
            for _ in range(z):
                # newlist.append(line[a+2])
                f.write(data[k][a+2] + ", ")
            a+=3
            pass
        except:
            # newlist.append(line[a+1])
            f.write(data[k][a+1] + ", ")
            a+=2
            pass
        pass
    f.write('\n')
    k+=1
