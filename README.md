# StockScraper
The StockScraper script can compile minute data of equities into a JSON or CSV file.

## Dependencies
- requests
- Python3

## Run Script 
Retreive an API Token from IEX cloud [here](https://iexcloud.io/cloud-login#/register/). Paste the API Token in `line 13` of `stockscraper.py`. Write your command as follows, and run the script in your command terminal.
```sh 
$ python3 path\to\stockscraper.py <symbol> <startdate format="yyyymmdd"> <businessdays options="Natural numbers only"> <format options="json/csv"> <filename>
```
### Example:
```sh
$ python3 stockscraper.py spy 20190603 5 csv spy-june
```
