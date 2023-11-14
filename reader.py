import pandas as pd
import math
from pdf2 import invoice_creator

client_data = pd.read_excel('Ноябрь новый лккк.xlsx')
#client_datas = pd.DataFrame('Ноябрь новый лк.xlsx')
#print(client_data.head(10))
NoOfInvoice = 1626
for index, row in client_data.iterrows():
    print(index, row)
    count = int(row['count'])
    tariff = int(row['tariff'])
    discount = row['скидка']
    if math.isnan(discount):
        discount = 0
    else:
        discount = int(discount)
    total = int(tariff * count - discount)
    print(row['inn'])
    inn = row['inn']
    legal_name = row['legal_name']

    email = row['email']
    if total > 0:
        invoice_creator(count, tariff, total, inn, legal_name, NoOfInvoice, discount, email)
        NoOfInvoice += 1
    print(f'printin NoOfInv {NoOfInvoice}')