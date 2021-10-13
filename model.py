import pymongo
import json
import requests
from pymongo import MongoClient #python driver for mongodb
import pandas as pd
import numpy as np
import math
from datetime import datetime, timezone
pd.set_option('display.max_columns', None) 
### DATASET ###

uri = ('mongodb://bdt2021:sM6F12Mh76lOuAcDdwmsfhFAfSQWZAFeibdvRzsqgg5ujdltmn9rCoAWpVh3vzlJ1of5KnJHAgarzpjRpZQ0KA==@bdt2021.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@bdt2021@')
client = pymongo.MongoClient(uri)

#d = dict((db, [collection for collection in client[db].list_collection_names()]) for db in client.list_database_names())
#s = json.dumps(d)
db = client.bdt2021

### BTC_test
btc = pd.DataFrame(columns=['volume_btc','price'])
for doc in db.bitcoin.find():
    row = {
    'volume_btc':doc['quote']['USD']['volume_24h'],
    'price':doc['quote']['USD']['price'] }
    print(doc)
    break

    #'date':doc['quote']['USD'][]}
    btc = BTC_test.append(row, ignore_index = True)

'''
### NASDAQ 
NSQ_test = pd.DataFrame(columns=['Close_NSQ'])
for doc in db.nasdaq.find():
    print(doc)
    #row= {'Close_NSQ':doc['previousClose']}
    #NSQ_test = NSQ_test.append(row, ignore_index = True)

### SP500
SP_test = pd.DataFrame(columns=['Close_SP500'])
for doc in db.sp500.find():
    row= {'Close_SP500':doc['previousClose']}
    SP_test = SP_test.append(row, ignore_index = True)

### DOW
DOW_test = pd.DataFrame(columns=['Close_DOW'])
for doc in db.dji.find():
    row= {'Close_DOW':doc['previousClose']}
    DOW_test = DOW_test.append(row, ignore_index = True)

### NYSE 
NYSE_test = pd.DataFrame(columns=['Close_NYSE'])
for doc in db.nyse.find():
    row= {'Close_NYSE':doc['previousClose']}
    NYSE_test = NYSE_test.append(row, ignore_index = True)

### VIX
VIX_test = pd.DataFrame(columns=['Close_VIX'])
for doc in db.vix.find():
    row= {'Close_VIX':doc['previousClose']}
    VIX_test = VIX_test.append(row, ignore_index = True)

##CHINA
CHI_test = pd.DataFrame(columns=['Close_China'])
for doc in db.china.find():
    row= {
    'Close_China':doc['previousClose']}
    CHI_test = CHI_test.append(row, ignore_index = True)

##RUSSIA
RU_test = pd.DataFrame(columns=['Close_Russia'])
for doc in db.russia.find():
    print(doc)
    break
    #row= {
    #'Close_Russia':doc['previousClose']}
    #RU_test = RU_test.append(row, ignore_index = True)

##ETHEREUM
ETH_test = pd.DataFrame(columns=['Close_ETH'])
for doc in db.ethereum.find():
    print(doc)
    row= {'Close_ETH':doc['quote']['USD']['price']}
    ETH_test = ETH_test.append(row, ignore_index = True)

##CARDANO
CAR_test = pd.DataFrame(columns=['Close_CAR'])
for doc in db.cardano.find():
    print(doc)
    break
    #row= {'Close_CAR':doc['quote']['USD']['price']}
    #CAR_test = CAR_test.append(row, ignore_index = True)

test = pd.concat([BTC_test, NSQ_test, SP_test, DOW_test, NYSE_test, VIX_test, 
CHI_test, RU_test, ETH_test, CAR_test], join ='inner', axis=1)'''
