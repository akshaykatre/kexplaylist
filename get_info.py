import pyquery
from pyquery import PyQuery
import datetime as DT
from datetime import datetime
from pytz import timezone
import kexp_url
import urllib2

def get_info(link):
    print "link: ", link

    try:
    
        query = PyQuery(link)
    except urllib2.HTTPError:
        return None, None, None, None,None, None

    tracks, artists =  [query(track).text().encode('utf-8') for track in query("div.TrackName")], [query(artist).text().encode('utf-8') for artist in query("div.ArtistName")]

    hostname, showname = [query("div.HostNames").text()]*(len(artists)), [query("div.ShowName").text()]*(len(artists))
#    print tracks, artists,hostname,showname
    date, time = [query("div.ShowAirDate").text()[:-6]]*(len(artists)), ([query(time).text() for time in query("div.AirDate")])
#    print tracks, artists, hostname, showname, date, time
    tracks.reverse()
    artists.reverse()
    hostname.reverse()
    showname.reverse()
    date.reverse()
    time.reverse()
    return tracks, artists, hostname, showname, date, time

def convert_to_hours(days):
    return days*24

def get_all(start_date_eu, end_date_eu):
    
    all_artists, all_tracks, all_hosts, all_shows, all_date, all_time = [], [] ,[], [], [], []

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
        # while link!=None:
        #     link = kexp_url.get_url(date=now.day, month=now.month, year=now.year, time=now.hour)
        print "link: ", link
        print "end: ", end
        
        tracks, artists, hostname, showname, date, time = get_info(link)
        
        while tracks == None:
            tracks, artists, hostname, showname, date, time = get_info(link)

        all_tracks += tracks
        all_artists += artists
        all_hosts += (hostname)
        all_shows += (showname)
        all_date += (date)
        all_time += (time)
 
        end = end + delta   
    
    return all_tracks, all_artists, all_hosts, all_shows, all_date, all_time
