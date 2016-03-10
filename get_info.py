""" This module collects information from kexp sorts them in arrays and returns 
complete arrays to kexplayist to be filled into a table """ 

from pyquery import PyQuery
import datetime as DT
#from datetime import datetime
from pytz import timezone
import kexp_url
import urllib2

def get_info(link):
    
    """ Query from kexp for infomation and 
    collect in arrays to return to get_all """ 
    print "link: ", link
    

    try:
    
        query = PyQuery(link)
    except urllib2.HTTPError:
        return None, None, None, None, None, None

    tracks =  [(query(track).text()).encode('utf-8') 
               for track in query("div.TrackName")]
    artists = [(query(artist).text()).encode('utf-8') 
               for artist in query("div.ArtistName")]

    hostname = [query("div.HostNames").text()]*(len(artists))
    showname = [query("div.ShowName").text()]*(len(artists))
#    print tracks, artists,hostname,showname
    date = [query("div.ShowAirDate").text()[:-6]]*(len(artists))
    time = [query(time).text() for time in query("div.AirDate")]
#    print tracks, artists, hostname, showname, date, time
    tracks.reverse()
    artists.reverse()
    hostname.reverse()
    showname.reverse()
    date.reverse()
    time.reverse()
    return tracks, artists, hostname, showname, date, time

# def convert_to_hours(days):
#     return days*24

def get_pac_time(start_date_eu, 
             end_date_eu):
    """ Calculate time in pacific zone """ 
    eutime = timezone('Europe/Amsterdam')
    pacific = timezone('US/Pacific')

    loc_st_dt = eutime.localize(start_date_eu)
    loc_ed_dt = eutime.localize(end_date_eu)
    
    st_dt_pac = loc_st_dt.astimezone(pacific)
    ed_dt_pac = loc_ed_dt.astimezone(pacific)
    
#    delta_days = abs(st_dt_pac - ed_dt_pac).days
    # if delta_days == 0:
    #     delta_min = abs(start_date_eu - end_date_eu).seconds
    #     print delta_min
    #     if delta_min > 0:
    #         delta_hours = delta_min/(60*60)
    # else:
    #     delta_hours = convert_to_hours(delta_days) 


    
#    now = datetime.now(pac)

    return ed_dt_pac, st_dt_pac

def get_all(start_date_eu, 
            end_date_eu):
    """ Return the arrays with all the information to fill tables """ 

    ed_dt_pac, st_dt_pac = get_pac_time(start_date_eu, end_date_eu)
    all_artists, all_tracks, all_hosts = [], [], [] 
    all_shows, all_date, all_time = [], [] , []

   # end = st_dt_pac
    delta = DT.timedelta(hours=1)

    print "end date is: ", ed_dt_pac
    while st_dt_pac != ed_dt_pac:
        now = st_dt_pac
        link = kexp_url.get_url(date=now.day, month=now.month, 
                                year=now.year, time=now.hour)

        print "link: ", link
#        print "end: ", end
        
        tracks, artists, hostname, showname, date, time = get_info(link)
        
        while tracks == None:
            tracks, artists, hostname, showname, date, time = get_info(link)

        all_tracks += tracks
        all_artists += artists
        all_hosts += (hostname)
        all_shows += (showname)
        all_date += (date)
        all_time += (time)
 
        st_dt_pac = st_dt_pac + delta   
    
    return all_tracks, all_artists, all_hosts, all_shows, all_date, all_time
