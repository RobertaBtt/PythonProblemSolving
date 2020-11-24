from random import randint

import await as await
import time
import asyncio
from timeit import default_timer as timer


#odds       function    <function odds at 0x7f329e8316d0>
def odds (start, stop):
    for odd in range(start, stop +1, 2):
        yield odd
        #Return the first value, and then pause,
        # Generator can pause execution anr resume any time later

#Syncronous version of Get Random Intereg Numbers
def randn():
    time.sleep(3)
    return randint(1,10)

async def async_randn():
    await asyncio.sleep(3)
    return randint(1,10)

async def main():
    odd_values = [odd for odd in odds(3,15)]
    odds2 = tuple(odds(21,29))
    print(odd_values)
    print(odds2)
    await async_randn()
    start = timer()
    print("A Random Sync: ", randn())
    end = timer()
    print((end - start) )  # Time in seconds, e.g. 5.3809195


    start = timer()
    print("A Random Async: ", await async_randn())
    end = timer()
    print((end - start) *10)  # Time in seconds, e.g. 5.3809195



if __name__ == "__main__":

    asyncio.run(main())


# Coroutintes are similar to generator, can be start, stop and pause
# Coroutines are mor consumers of data

#g = odds(3,15)
#print(next(g))
# puts every value of the generator into the list
#print(list(g))
