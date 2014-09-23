import os
import csv
from collections import Counter
from operator import itemgetter
from prettytable import PrettyTable

CSV_FILE = os.path.join("/Users")
j = 0
#CSV_FILE = open("my_connections.csv","r")

transforms = [(', Inc.', ''), (', Inc', ''), (', LLC', ''), (', LLP', ''),
               (' LLC', ''), (' Inc.', ''), (' Inc', '')]

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]
companies = [c['Company'].strip() for c in contacts if c['Company'].strip() != '']

for i, _ in enumerate(companies):
    for transform in transforms:
        companies[i] = companies[i].replace(*transform)
        j += 1

pt = PrettyTable(field_names=['Company', 'Freq'])
pt.align = 'l'
c = Counter(companies)
[pt.add_row([company, freq]) 
 for (company, freq) in sorted(c.items(), key=itemgetter(1), reverse=True) 
     if freq > 30]

print "The top three companies in my network are"
print pt

print "The number of companies in my linkedin network is", len(companies)

print "The number of times a company is mentioned in my connections is",j
