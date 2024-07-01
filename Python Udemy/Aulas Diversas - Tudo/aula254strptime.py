# Datetime Strptime 

from datetime import datetime

fmt = "%d/%m/%Y"

data = datetime.strptime("1958-03-05", "%Y-%m-%d")
print( data.strftime(fmt))