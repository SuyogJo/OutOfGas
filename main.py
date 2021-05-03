import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://etherscan.io/txs'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

dfs = pd.read_html(r.text, index_col=2)

print(dfs)

df = dfs[0]
df.head()

df = df.replace({'Ether': ''}, regex=True)
df['Value'] = df['Value'].apply(pd.to_numeric)
df.info()

plt.style.use('seaborn-whitegrid')
df.plot.bar(x='Value', y=['Unnamed: 9'])
plt.show()