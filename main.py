# Dependências
import pandas as pd
from flask import Flask, render_template

# Inicializador do Flask
app = Flask(__name__, template_folder='') 

tabela = pd.read_csv("BitCoin.csv")

# Páginas do Site
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/mediavolume')
def mediaVolume():
  mediaVolume = tabela["btc_trade_volume"].mean()

  output1 = {'mediaVolume': mediaVolume}

  return output1

# Rota
if __name__ == "__main__":
  app.run(host = '0.0.0.0')