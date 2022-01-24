import pandas as pd
from flask import Flask

app = Flask(__name__) 

@app.route("/")
def home():
  tabela = pd.read_csv("BitCoin.csv")

  mediaVolume = tabela["btc_trade_volume"].mean()

  output1 = {'mediaVolume': mediaVolume}

  return output1

app.run(host = '0.0.0.0')