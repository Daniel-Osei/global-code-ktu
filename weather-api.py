import pyowm

owm = pyowm.OWM('6cfa4b190d1857e56f19a72ccd7219d1')
fc = owm.three_hours_forecast('Cape Coast, Ghana')
f = fc.get_forecast()

for weather in f:
	print (weather.get_reference_time('iso'), weather.get_status())
