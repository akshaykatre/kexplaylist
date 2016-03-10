"""This is the main module of kexplaylist """


from datetime import datetime
#import prettytable
#from build_table import build_tables
from get_info import get_all
from build_table_df import build_tables_df

def Run_playlist(START_DATE=None, END_DATE=None, out_type='csv'):
    if START_DATE == None:
        START_DATE = datetime(2014, 1, 01, 19)
        END_DATE = datetime(2014, 1, 20, 22)

    print START_DATE, END_DATE
        
    TRACKS, ARTISTS, HOSTNAME, SHOWNAME, DATE, TIME = get_all(START_DATE, END_DATE)
# all_tracks.append(tracks)
# all_artitsts.append(artists)
# all_hostnames(hostname)
# all_shownames(showname)


    TABLES = build_tables_df(ARTISTS, TRACKS, SHOWNAME, HOSTNAME, DATE, TIME)
    print TABLES
    
    if out_type == 'csv':
        TABLES.to_csv("output.csv")
    elif out_type == 'excel':
        TABLES.to_excel("output.xls")

#tables.set_style(MSWORD_FRIENDLY)
