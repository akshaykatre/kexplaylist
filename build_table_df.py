import pandas
from pandas import DataFrame as df

def build_tables_df(artists, tracks, showname, host,date,time):
    dataf = df({'Artists': artists, 'Tracks':tracks, 'Showname':showname, 'Host':host, 'date':date,'time':time})
    return dataf
