'''find the link in the csv file
The link should be: 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'
'''

import csv
import request

data = open('find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
data.close()

length = len(data_lines)
HTTP_list =[]
for i in range(length):
    HTTP_list.append(data_lines[i][i])
    pdf_address = ''.join(item for item in HTTP_list)

print(pdf_address)


