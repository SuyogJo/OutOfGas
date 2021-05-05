import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'https://etherscan.io/txs'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)


nonZeroValue = []
nonZeroGas = []



while len(nonZeroValue) <= 50:
  dfs = pd.read_html(r.text, index_col=2)
  #print(dfs)
  df = dfs[0]
  df.head()
  df = df.replace({'Ether': ''}, regex=True)
  df['Value'] = df['Value'].apply(pd.to_numeric)
  transacValue = (df['Value'])
  gasPrice = (df['Unnamed: 9'])

  for i in range(len(transacValue)):
    if (transacValue[i] != 0 and transacValue[i] <= 3):
      nonZeroValue.append(transacValue[i])
      nonZeroGas.append(gasPrice[i])
    else:
      pass

print(nonZeroValue)
print(nonZeroGas)


nonZeroVal = np.asarray(nonZeroValue)
nonZeroG = np.asarray(nonZeroGas)

m, b = np.polyfit(nonZeroValue, nonZeroGas, 1)

plt.style.use('seaborn-whitegrid')
plt.scatter(nonZeroVal, nonZeroG)
plt.plot(nonZeroVal, m*nonZeroVal + b)
plt.title("The relationship between the transaction value and the gas prices \nnot including 0 ETH transactions")
plt.xlabel("Values of the Transaction in ETH")
plt.ylabel("Gas Values in ETH")
plt.show()

