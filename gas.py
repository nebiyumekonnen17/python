
fuel_level = 10

low_fuel_threshold = 15

if fuel_level <= 0:
    print("Tank is EMPTY")
elif fuel_level < low_fuel_threshold:
    print("Low fuel warning ON")
else:
    print("Fuel level is OK")
