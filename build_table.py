import prettytable
from prettytable import PrettyTable

def build_tables(artists, tracks, showname, host, date, time):
    table = PrettyTable()
    fmt = '%Y-%b-%d %H H %Z%z'
#    table.add_column("Date", [now.strftime(fmt)]+['']*(len(artists)-1))
    table.add_column("Show Name", showname)
    table.add_column("Host Name", host)
    table.add_column("Artists", artists)
    table.add_column("Tracks" , tracks)
    table.add_column("Date", date)
    table.add_column("Time", time)
    return table
