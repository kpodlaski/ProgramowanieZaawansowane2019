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


def count_avg_in_month(kursy, month):
    #wyszukiwanie rekordów w stuczniu 2019
    m_kursy = kursy.loc[kursy.data<'20190200']
    m_kursy = m_kursy.loc.loc[kursy.data>'20190100']
    print(m_kursy)

if __name__=="__main__":
    kursy = pd.read_csv("../data/nbp_kursy_2019.csv"
                        , delimiter=";",
                        encoding="cp1250",
                        decimal=",",
                        engine="python"
                        )
    #proste_operacje(kursy)
    count_avg_in_month(kursy,1)

## Zadania do wykonania:
## Policzyć średnią w miesiącu (I-IX, 2019)
## Odchylenie standardowe w każdym miesiącu (I-IX, 2019)
## Policzyć średnią kwartalną (QI,QII,QIII, 2019)
## Odchylenie standardowe w każdym kwartale (QI,QII,QIII, 2019)
## Który miesiąc  największe zmiany
## Który kwartał najdroższy/najtanszy

