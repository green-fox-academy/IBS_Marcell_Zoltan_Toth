from petrol_station_package11.station import Station
from petrol_station_package11.car import Car


OMW = Station()
BMW = Car()

OMW.refill(BMW)

print(BMW.gas_amount)
print(OMW.gas_amount)