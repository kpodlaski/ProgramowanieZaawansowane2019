import pandas as pd

def proste_operacje(kursy):
    print(kursy)
    print(kursy.columns)
    # print(kursy[['data','1USD']])
    # print(kursy[['1USD']][0:-2].min())
    usd = kursy['1USD'][2:-3].astype('float64')
    print(usd)
    row_id = usd.idxmin()
    print(kursy.loc[row_id]['data'])



kursy = pd.read_csv("../data/nbp_kursy_2019.csv"
                    ,delimiter=";",
                    encoding="cp1250",
                    decimal=",",
                    engine="python"
                    )
## Zadania do wykonania:
## Policzyć średnią w miesiącu (I-IX, 2019)
## Odchylenie standardowe w każdym miesiącu (I-IX, 2019)
## Policzyć średnią kwartalną (QI,QII,QIII, 2019)
## Odchylenie standardowe w każdym kwartale (QI,QII,QIII, 2019)
## Który miesiąc  największe zmiany
## Który kwartał najdroższy/najtanszy

