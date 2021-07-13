import csv
f = open("csv/SOCR-HeightWeight.csv", newline = "")
reader = csv.reader(f)
filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))
n = len(newdata)
total = 0
for x in newdata:
    total = total + x
mean = total/n
print(mean)