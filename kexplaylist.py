import pyquery 
from pyquery import PyQuery
import kexp_url
from datetime import datetime
import prettytable
from build_table import build_tables
from pytz import timezone
from get_info import get_info, get_all


start_date = datetime(2014, 1, 9, 0)
end_date = datetime(2014, 1, 9, 6)

tracks, artists, hostname, showname = get_all(start_date, end_date)
# all_tracks.append(tracks)
# all_artitsts.append(artists)
# all_hostnames(hostname)
# all_shownames(showname)


tables = build_tables(artists, tracks)
