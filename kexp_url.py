""" Returns the url that needs to be queried """ 

def get_time(hour):
    """ Sort time in 12 hour format """ 
    meri = "AM"
    if hour > 12:
        hour = hour - 12
        meri = "PM"
    return hour, meri


def get_url(date=None, month=None, year=None, time=None):
    """ Estimate the url based on inputs of date and time """ 
    url = "http://kexp.org/playlist"

    if date != None:
        time, meri = get_time(time)
        print date, month, year, time, meri
        url += '/'+str(year)
        url += '/'+str(month)
        url += '/'+str(date)
        url += '/'+str(time)
        url += str(meri)

    return url
