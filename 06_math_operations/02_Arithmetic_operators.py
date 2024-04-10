first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)


# Convert strings to numbers

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)


# Absolute values
print(32-16)
print(abs(16-32))


# Rounding

print(round(1.4))
print(round(1.454545,3))


# CEIL() and FLOOR()

from math import ceil, floor

print(ceil(12.5))
print(floor(12.5))