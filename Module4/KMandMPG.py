def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 1 / 1.609344
    
    return (miles / gallons) * 100

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    km = miles * 1.609344
    
    return (liters / km) * 100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))


print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))