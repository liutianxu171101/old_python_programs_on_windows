import csv
data = []
f = open('数据1.csv','r',newline = '',encoding = 'utf-8')
csv_reader = csv.reader(f)
for row in csv_reader:
    data.append(float(row[0]))

f.close()

f = open('generate.csv','w',newline = '',encoding = 'utf-8')
csv_writer = csv.writer(f)
for i in range(0,24):
    sbuf = []
    for j in range(0,10):
        sbuf.append(data[10*i+j])

    csv_writer.writerow(sbuf)
f.close()

data = []
f = open('数据2.csv','r',newline = '',encoding = 'utf-8')
csv_reader = csv.reader(f)
for row in csv_reader:
    data.append(float(row[0]))

f.close()

f = open('transport.csv','w',newline = '',encoding = 'utf-8')
csv_writer = csv.writer(f)
for i in range(0,24):
    sbuf = []
    for j in range(0,3):
        sbuf.append(data[3*i+j])

    csv_writer.writerow(sbuf)
f.close()

