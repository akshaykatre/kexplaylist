import pyquery 
from pyquery import PyQuery
import kexp_url
from datetime import datetime
import prettytable
from build_table import build_tables
from pytz import timezone
from get_info import get_info, get_all
from prettytable import MSWORD_FRIENDLY
from build_table_df import build_tables_df
start_date = datetime(2014, 1, 20, 19)
end_date = datetime(2014, 1, 20, 22)

tracks, artists, hostname, showname, date, time = get_all(start_date, end_date)
# all_tracks.append(tracks)
# all_artitsts.append(artists)
# all_hostnames(hostname)
# all_shownames(showname)


tables = build_tables_df(artists, tracks, showname, hostname, date, time)
#tables.set_style(MSWORD_FRIENDLY)
