from flights.txt import Source

class Outgoing(Source)
def mapper(self, key, line)
Destination = line.split
for d in Destination:
    yield (d,1)
  
def reducer (self, key, values)
