import pandas as pd

kursy = pd.read_csv("../data/nbp_kursy_2019.csv"
                    ,delimiter=";",
                    encoding="cp1250",
                    decimal=",",
                    engine="python"
                    )
print(kursy)
print(kursy.columns)
#print(kursy[['data','1USD']])
#print(kursy[['1USD']][0:-2].min())
usd = kursy['1USD'][2:-3].astype('float64')
print(usd)
row_id = usd.idxmin()
print(kursy.loc[row_id]['data'])