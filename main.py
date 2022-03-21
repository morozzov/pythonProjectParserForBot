import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from quote import Quote
import json
from bs4 import BeautifulSoup
import requests as req

engine = create_engine('postgresql+psycopg2://User:Password@Host/Database')

Session = sessionmaker(bind=engine)
session = Session()

def parseQuote():
    resp = req.get("http://bashorg.org/random")
    text = BeautifulSoup(resp.text, 'lxml')
    number = BeautifulSoup(resp.text, 'html.parser')
    text = text.find("div", class_="quote").getText(separator="\n")
    number = number.find("div", class_="vote").a.getText().split('#')[1]

    return (number, text)

for i in range(0, 100):
    tempQuote = parseQuote()
    newQuote = Quote(number=tempQuote[0], text=tempQuote[1])
    session.add(newQuote)
    session.commit()

print(parseQuote()[0])