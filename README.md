Creta helps you predict the execution time of your loops.

#Creta?
Creta is an island in the mediteranean however it also reads as:

* Continously
* Recalculated
* Estimated
* Time of
* Arrival

And creta does this in the most laxy way possible (cliffhanger resolved by looking in the code :-)

#Usage
By default creta will not interfere with your loops, so it will continue forever. 
This behaviour is controlled by the "strict" flag, if True it will raise StopIteration on end destination.

##Use creta as a context manager:
Directly relying on its builtin iterator:

    With creta.ETA(10, strict=True) as eta:
        For s in eta:
            Print s
            Time.sleep(1)

Or just using its functionality for info
    
    n = 100
    with creta.ETA(10) as eta:
        for i in range(n):
            do_heavy_work(i)
            print "still working: {}".format(eta.update()) # or next(eta)

## Use creta as an iterator

    eta = creta.ETA(10, strict=True)
    print eta.update()
    print next(eta)
    print [s for s in eta]
    next(eta) 
    >>> StopIteration !!!
    
#License
creta is released under the MIT license.

If you happen to use it on a daily basis then please wear a hat while you sleep.

