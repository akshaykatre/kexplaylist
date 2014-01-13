def get_time(hour):
    meri = "AM"
    if hour > 12:
        hour = hour - 12
        meri = "PM"
    return hour, meri


def get_url(date=None, month=None, year=None, time=None):
    url = "http://kexp.org/playlist"

    if date != None:
        time, meri = get_time(time)
        url = url+'/'+str(year)+'/'+str(month)+'/'+str(date)+'/'+str(time)+str(meri)

    return url
