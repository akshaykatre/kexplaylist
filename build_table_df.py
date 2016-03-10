#import pandas
""" build_tables_df returns the data in a DataFrame format to kexplaylist """

from pandas import DataFrame as df

def build_tables_df(artists, tracks, showname, host, date, time):
    """ This function sorts the data into a DataFrame from the pandas module """
    dataf = df({'Artists': artists, 'Tracks':tracks, 'Showname':showname, 
                'Host':host, 'date':date, 'time':time})
    return dataf
