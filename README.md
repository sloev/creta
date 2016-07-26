Creta helps you predict the execution time of your loops.

Creta reads as:

* Continously
* Recalculated
* Estimated
* Time of
* Arrival


Usage

By default creta will not interfere with your loops, so it will continue forever. 
This behaviour is controlled by the "strict" flag.

Use creta as a context manager:

With creta.ETA(10) as eta:
    For s in eta:
        Print s
        Time.sleep(1)

