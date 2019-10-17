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

def stats_for_dataframe(kursy, start_date, end_date):
    m_kursy = kursy.loc[kursy.data < end_date]
    m_kursy = m_kursy.loc[kursy.data > start_date]
    mean # = policzyć
    std # = pliczyć
    return mean, std

def count_avg_in_month(kursy, year, month):
    start_date= '{0}{1:02d}{2:02d}'.format(year,month,0)
    if month == 12 :
        end_date = '{0}{1:02d}{2:02d}'.format(year+1,0,0)
    else :
        end_date = '{0}{1:02d}{2:02d}'.format(year, month+1, 0)


    return stats_for_dataframe(kursy, start_date, end_date)

if __name__=="__main__":
    kursy = pd.read_csv("../data/nbp_kursy_2019.csv"
                        , delimiter=";",
                        encoding="cp1250",
                        decimal=",",
                        engine="python"
                        )
    #proste_operacje(kursy)
    mean, std = count_avg_in_month(kursy,2019, 1)
    print(mean, " : ", std)


## Zadania do wykonania:
## Policzyć średnią w miesiącu (I-IX, 2019)
## Odchylenie standardowe w każdym miesiącu (I-IX, 2019)
## Policzyć średnią kwartalną (QI,QII,QIII, 2019)
## Odchylenie standardowe w każdym kwartale (QI,QII,QIII, 2019)
## Który miesiąc  największe zmiany
## Który kwartał najdroższy/najtanszy

