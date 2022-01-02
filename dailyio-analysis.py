import csv

with open('daylio_export_2021_12_26.csv') as daylioFile:
    reader = csv.reader(daylioFile)
    count2021, count2020, count2019, count2018, count2017, count2016 = 0, 0, 0, 0, 0, 0
    eachRow = []
    for row in reader:
        eachRow.append(row)
        characteristics = str.lower(row[5])
        stringValue = str(row[0])
        if(str.startswith(stringValue, '2021') and ('took meds' in characteristics)):
            count2021+=1
        elif(str.startswith(stringValue, '2020') and ('took meds' in characteristics)):
            count2020+=1
        elif(str.startswith(stringValue, '2019') and ('took meds' in characteristics)):
            count2019+=1
        elif(str.startswith(stringValue, '2018') and ('took meds' in characteristics)):
            count2018+=1
        elif(str.startswith(stringValue, '2017') and ('took meds' in characteristics)):
            count2017+=1
        elif(str.startswith(stringValue, '2016') and ('took meds' in characteristics)):
            count2016+=1
    print('The number of rows for 2021 are ' +str(count2021/361))
    print('The number of rows for 2020 are ' +str(count2020/366))
    print('The number of rows for 2019 are ' +str(count2019/366))
    print('The number of rows for 2018 are ' +str(count2018/366))
    print('The number of rows for 2017 are ' +str(count2017/366))
    print('The number of rows for 2016 are ' +str(count2016/366))
