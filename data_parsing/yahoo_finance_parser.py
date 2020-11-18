# -*- coding: utf-8 -*-
"""
Created on 17 Nov 2020
@author: Peruski
"""

#import pandas as pd
from bs4 import BeautifulSoup
import requests

def getPricing(tickers):

    tckr_data = {}
    
    for tckr in tickers:
        url = 'https://finance.yahoo.com/quote/' + tckr
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #soup2.find_all('span', class_="Trsdu(0.3s)")
        pe_ratio = float(soup.find(True, {'class' : "Trsdu(0.3s)", 'data-reactid' : "149"}).text)
        price = float(soup.find(True, {'class' : "Trsdu(0.3s)", 'data-reactid' : "50"}).text)
        prev_close = float(soup.find(True, {'class' : "Trsdu(0.3s)", 'data-reactid' : "98"}).text)
        
        tckr_data.update({tckr :
                          {'pe_ratio' : pe_ratio,
                          'price' : price,
                          'prev_close' : prev_close}})
        
    return(tckr_data)

#getPricing(['MSFT', 'AAPL', 'JPM'])
