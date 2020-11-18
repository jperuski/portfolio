
library(reticulate)
library(data.table)
library(foreach)
library(ggplot2)

## Select a conda environment and source the .py file containing the Yahoo! Finance parser
use_condaenv("tf2")
source_python('C:\\Users\\jcp5z\\Documents\\GitHub\\portfolio\\data_parsing\\yahoo_finance_parser.py')

## Define a wrapper function for:
## - Calling getPrcing
## - Converting the dict/named list output to data.table
getPricingR <- function(tickers) {
  
  raw_val <- getPricing(tickers)
  valuation <- foreach(tt = tickers, .combine = "rbind") %do% {
    
    t_val <- data.table(ticker = tt,
                        price = raw_val[[tt]]$price,
                        prev_close = raw_val[[tt]]$prev_close,
                        pe_ratio = raw_val[[tt]]$pe_ratio)
    
    return(t_val)
  }  
}

## Scrape, parse and format the valuation data
tickers <- list("MSFT", "JPM", "AAPL")
valuation <- getPricingR(tickers)

print(valuation)
