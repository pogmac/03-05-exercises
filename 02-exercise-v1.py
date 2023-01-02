def build_bridge(chunk,goal):
    nchunk = 1
    nconnectors = 0
    #bLength = chunk # case 1 when the bridge consists of only one chunk 
    bLength = chunk
    if(bLength == goal):
        return True
    while (bLength <= goal): # case 2 when the bridge consists of chunk + n * (1.5 * chunk)
        bLength = bLength + 1.5*chunk
        nchunk = nchunk + 1
        nconnectors = nconnectors +1
        if(bLength == goal):
            print("Number of chunks = ", nchunk , "chunks length = " , nchunk*chunk)
            print("Number of connectors = ", nconnectors , "connectors length = " , nconnectors*chunk/2 )
            print("Bridge length = ", bLength)
            return True
        elif(bLength > goal):
            print("Number of chunks = ", nchunk , "chunks length = " , nchunk*chunk)
            print("Number of connectors = ", nconnectors , "connectors length = " , nconnectors*chunk/2 )
            print("Bridge length = ", bLength, "instead of a length = ", goal)
            return False
        else:
            pass
    
if (build_bridge(5,65)):
    print("Success")
else:
    print("Failure")    

"""
Rozważ taki kod:

junction = chunk / 2

Przyda się też:

x = (goal + (junction * 1))/(chunk + junction)

Co zwracamy?

return True if x.is_integer() else False
"""