# fin-import

Simple python script to retrieve financial data (stock data)

Retrieves a specific stock's value for a specified period of time and exports it to a text file

**DISCLAIMER! - This project was made for learning purposes and to be used in a personal project. I don't suggest using this for anything, there are much better tools out there.**

## Installation:
```
git clone https://github.com/minikempe/fin-import
cd fin-import
python -m venv venv
```
Unix:
`source venv/Scripts/activate`  
Windows (cmd):
`venv\Scripts\activate.bat`  
Windows (PS):
`venv\Scripts\Activate.ps1`
```
python -m pip install -r requirements.txt
python fin-import
```

## Usage
`python fin-import [options...] symbol`

```
fin-import [-h] [-s START] [-e END] symbol

positional arguments:
  symbol                    Stock symbol (Ticker)

options:
  -h, --help                show this help message and exit
  -s START, --start START   Start date [YYYY-MM-DD] (default: 2010-01-01)
  -e END, --end END         End date [YYYY-MM-DD] (default: today)
```
