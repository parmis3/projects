import math

limit = 10000
out = 0
i=0

while i < limit:
    out = out + (1 / (i ** 2))
    i = i + 1

pi_approximate = math.sqrt(out*6 )
print(pi_approximate)
print(math.pi)
