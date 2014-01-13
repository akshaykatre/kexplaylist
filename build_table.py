import prettytable
from prettytable import PrettyTable

def build_tables(artists, tracks):
    table = PrettyTable()
    fmt = '%Y-%b-%d %H H %Z%z'
#    table.add_column("Date", [now.strftime(fmt)]+['']*(len(artists)-1))
#    table.add_column("Show Name", [showname]+['']*(len(artists)-1))
#    table.add_column("Host Name", [host]+['']*(len(artists)-1))
    table.add_column("Artists", artists)
    table.add_column("Tracks" , tracks)

    return table
