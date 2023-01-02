def build_bridge(chunk,goal):
    connector = chunk/2
#    x = (goal+connector)/(chunk + connector)
#    return True if x.is_integer() else False
    y = (goal+connector) % (chunk + connector)
    return True if y == 0 else False

if (build_bridge(4,65)):
    print("Success")
else:
    print("Failure")    

#2*6 + 1*5 = 17
#18 +1 % 3 = 0 
"""
Rozważ taki kod:

junction = chunk / 2

Przyda się też:

x = (goal + (junction * 1))/(chunk + junction)

Co zwracamy?

return True if x.is_integer() else False
"""