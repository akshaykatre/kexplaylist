import pyquery
from pyquery import PyQuery
import datetime as DT
from datetime import datetime
from pytz import timezone
import kexp_url

def get_info(link):
    query = PyQuery(link)
    tracks, artists =  [query(track).text() for track in query("div.TrackName")], [query(artist).text() for artist in query("div.ArtistName")]

    hostname, showname = query("div.HostNames").text(), query("div.ShowName").text()
#    print tracks, artists,hostname,showname

    return tracks, artists, hostname, showname

def convert_to_hours(days):
    return days*24

def get_all(start_date_eu, end_date_eu):
    
    all_artists, all_tracks, all_hosts, all_shows = [], [] ,[], []

    eutime = timezone('Europe/Amsterdam')
    pacific=timezone('US/Pacific')

    loc_st_dt = eutime.localize(start_date_eu)
    loc_ed_dt = eutime.localize(end_date_eu)
    
    st_dt_pac = loc_st_dt.astimezone(pacific)
    ed_dt_pac = loc_ed_dt.astimezone(pacific)
    
    delta_days = abs(st_dt_pac - ed_dt_pac).days
    if delta_days == 0:
        delta_min = abs(start_date_eu - end_date_eu).seconds
        print delta_min
        if delta_min > 0:
            delta_hours = delta_min/(60*60)
    else:
        delta_hours = convert_to_hours(delta_days) 


    
#    now = datetime.now(pac)
    end= st_dt_pac
    delta = DT.timedelta(hours=1)
    print "end date is: ", ed_dt_pac
    while end != ed_dt_pac:
        now = end
        link = kexp_url.get_url(date=now.day, month=now.month, year=now.year, time=now.hour)
        print "link: ", link
        print "end: ", end
        end = end + delta
        tracks, artists, hostname, showname = get_info(link)
        all_tracks += tracks
        all_artists += artists
        all_hosts.append(hostname)
        all_shows.append(showname)

    
    
    return all_tracks, all_artists, all_hosts, all_shows
