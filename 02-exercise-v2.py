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
