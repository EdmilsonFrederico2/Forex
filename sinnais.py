import pandas as pd
import yfinance as yf

# Baixar dados do par de moedas EUR/USD do Yahoo Finance
data = yf.download("EURUSD=X", start="2024-01-01", end="2024-01-07")

# Calcular médias móveis simples de curto e longo prazo (50 e 200 dias, por exemplo)
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Definir condições de compra e venda
data['Signal'] = 0  # Inicializa o sinal como neutro
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # Sinal de compra
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  # Sinal de venda

# Filtrar os sinais de compra e venda para o intervalo de datas desejado
buy_signals = data[data['Signal'] == 1].index
buy_signals_filtered = buy_signals[(buy_signals >= '2024-01-01') & (buy_signals <= '2024-01-10')]
sell_signals = data[data['Signal'] == -1].index
sell_signals_filtered = sell_signals[(sell_signals >= '2024-01-01') & (sell_signals <= '2024-01-10')]

# Mostrar sinais de compra e venda para 5 de janeiro de 2024
buy_signal_5_jan = buy_signals_filtered[buy_signals_filtered == '2024-01-08']
sell_signal_5_jan = sell_signals_filtered[sell_signals_filtered == '2024-01-08']

if not buy_signal_5_jan.empty:
    print("Sinal de compra em 5 de janeiro de 2024.")
    print("Recomendação de compra.")
else:
    print("Não há sinal de compra em 5 de janeiro de 2024.")

if not sell_signal_5_jan.empty:
    print("Sinal de venda em 5 de janeiro de 2024.")
    print("Recomendação de venda.")
else:
    print("Não há sinal de venda em 5 de janeiro de 2024.")
