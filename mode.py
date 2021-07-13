from collections import Counter
import csv
f = open("csv/SOCR-HeightWeight.csv", newline = "")
reader = csv.reader(f)
filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))
data = Counter(newdata)
modeRangeData = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for weight, occurence in data.items():
    if(75 < float(weight) < 85):
        modeRangeData["75-85"] = modeRangeData["75-85"] + occurence
    elif(85 < float(weight) < 95):
        modeRangeData["85-95"] = modeRangeData["85-95"] + occurence
    elif(95 < float(weight) < 105):
        modeRangeData["95-105"] = modeRangeData["95-105"] + occurence
    elif(105 < float(weight) < 115):
        modeRangeData["105-115"] = modeRangeData["105-115"] + occurence
    elif(115 < float(weight) < 125):
        modeRangeData["115-125"] = modeRangeData["115-125"] + occurence
    elif(125 < float(weight) < 135):
        modeRangeData["125-135"] = modeRangeData["125-135"] + occurence
    elif(135 < float(weight) < 145):
        modeRangeData["135-145"] = modeRangeData["135-145"] + occurence
    elif(145 < float(weight) < 155):
        modeRangeData["145-155"] = modeRangeData["145-155"] + occurence
    elif(155 < float(weight) < 165):
        modeRangeData["155-165"] = modeRangeData["155-165"] + occurence
    elif(165 < float(weight) < 175):
        modeRangeData["165-175"] = modeRangeData["165-175"] + occurence
    modeRange, modeOccurance = 0,0
for Range, Occurence in modeRangeData.items():
    if(Occurence > modeOccurance):
        modeRange, modeOccurance = [int(Range.split("-")[0]), int(Range.split("-")[1])], Occurence
mode = float((modeRange[0]+modeRange[1]) / 2)
print(mode)