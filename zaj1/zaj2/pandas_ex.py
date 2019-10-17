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
    usd = m_kursy['1USD'].astype('float64')
    return usd.mean(), usd.std(), usd.min(), usd.max()

def count_stats_in_month(kursy, year, month):
    start_date= '{0}{1:02d}{2:02d}'.format(year,month,0)
    if month == 12 :
        end_date = '{0}{1:02d}{2:02d}'.format(year+1,0,0)
    else :
        end_date = '{0}{1:02d}{2:02d}'.format(year, month+1, 0)
    return stats_for_dataframe(kursy, start_date, end_date)


def count_stats_in_quarter(kursy, year, q):
    start_date= '{0}{1:02d}{2:02d}'.format(year,3*q-2,0)
    if q == 4 :
        end_date = '{0}{1:02d}{2:02d}'.format(year+1,0,0)
    else :
        end_date = '{0}{1:02d}{2:02d}'.format(year, 3*q+1, 0)
    return stats_for_dataframe(kursy, start_date, end_date)

months = ['','styczen', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

if __name__=="__main__":
    kursy = pd.read_csv("../data/nbp_kursy_2019.csv"
                        , delimiter=";",
                        encoding="cp1250",
                        decimal=",",
                        engine="python"
                        )
    #proste_operacje(kursy)
    ##Średnia odchylenie standardowe w miesiącu
    maximal_change =0
    period_with_maximal_change = 0
    for m in range(1,13):
        mean, std, min, max = count_stats_in_month(kursy,2019, m)
        if (max - min) > maximal_change:
            maximal_change = max - min
            period_with_maximal_change = m
        print('Miesiąc {0}: śr={1:.3f}, odchylenie={2:.3f}'.format(months[m],mean,std))
    print('-------------')
    print('Najgorszy miesiąc {0}: zmiana={1:0.3f}'.format(months[period_with_maximal_change], maximal_change))
    print('-------------')
    maximal_change = 0
    period_with_maximal_change = 0
    for q in range(1,5):
        mean, std, min, max = count_stats_in_quarter(kursy,2019, q)
        print('Q{0}: śr={1:.3f}, odchylenie={2:.3f}'.format(q,mean,std))
        if (max - min) > maximal_change:
            maximal_change = max - min
            period_with_maximal_change = q
    print('-------------')
    print('Najgorszy kwartał Q{0}: zmiana={1:0.3f}'.format(period_with_maximal_change, maximal_change))
    print('-------------')


## Zadania do wykonania:
## Policzyć średnią w miesiącu (I-IX, 2019)
## Odchylenie standardowe w każdym miesiącu (I-IX, 2019)
## Policzyć średnią kwartalną (QI,QII,QIII, 2019)
## Odchylenie standardowe w każdym kwartale (QI,QII,QIII, 2019)
## Który miesiąc  największe zmiany
## Który kwartał najdroższy/najtanszy

