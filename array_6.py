# Importamo modul random
import random
# Iz knjižnice pip._vendor.msgpack.fallback importamo xrange
from pip._vendor.msgpack.fallback import xrange
# Programu sporočimo naj izbere 10 števil od 1 do 100
array = random.sample(xrange(101),10)
# Vpeljemo spremenljivko total in s funkcijo sum() seštejemo elemente "tabele"
total = sum(array)
# Izpišemo element
print(array)
# Izpišemo seštevek vsem elementov.
print(total)