import collections
import csv
from os import write

# Point = collections.namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)
# print(p.x)

with open('name.csv', 'w') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first': 'Mike', 'last': 'Jackson', 'address': 'A'})
    writer.writerow({'first': 'Yosh', 'last': 'Kasama', 'address': 'B'})
    writer.writerow({'first': 'Nancy', 'last': 'Mask', 'address': 'C'})

with open('name.csv', 'r') as f:
    csv_reader = csv.reader(f)
    # print(next(csv_reader))
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        names = Names._make(row)
        print(names.first, names.last, names.address)
