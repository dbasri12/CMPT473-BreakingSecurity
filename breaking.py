
from typing import Tuple
from time import perf_counter_ns
from string import ascii_lowercase

import scipy
import numpy

from e5utils import LockBox, Facade


# NOTE: Returns a pair (password, contents) corresponding to
#  the password that opens the lockbox and the actual contents of the
#  lockbox. The only action that it can take with a `LockBox` is
#  calling the `try_password` method. Any other properties (like
#  field names, number of fields, etc.) can change at test time.
def break_lockbox(lockbox: LockBox) -> Tuple[str, str]:
    #Initialize variable
    password=""
    result=None
    tempPass=""
    lastavgTime=2500
    counter=0
    avgTime_arr=[]

    #Loop until try_password return a value
    while result is None:
        for c in "abcdefghijklmnopqrstuvwxyz":
            totalTime_takes=0
            avgTime=0
            tempPass=password + c

            start_time=perf_counter_ns()
            result=lockbox.try_password(tempPass)
            end_time=perf_counter_ns()
            time_takes=end_time-start_time
            totalTime_takes += time_takes
            avgTime=totalTime_takes

            #print(avgTime) #Testing purposes

            if avgTime > lastavgTime*1.25:
                password=tempPass
                avgTime_arr.append(lastavgTime)
                lastavgTime=avgTime
                counter+=1
                break
            if c == "z":
                counter =counter - 1
                password=password[:(counter)]
                result=None
                lastavgTime=avgTime_arr[counter]
                del avgTime_arr[counter]
    
    """for j in range(1,20):
        print("length ",j)
        for i in range(1,10):
            password='open'
            start_time=perf_counter_ns()
            result=lockbox.try_password(password)
            end_time=perf_counter_ns()
            print(end_time-start_time)"""
    return (password, result)
    

# NOTE: Returns a string corresponding to the result from successfully
# calling `takeover` on a `CaerfilyDesinedSurvis`. 
def break_facade(facade: Facade) -> str:
    name='myName \n dumpcodeword'
    result=facade.greet(name)
    codeword=''
    if len(result)>0:
        codeword=result[1]

    name='myName \n takeover {}'.format(codeword)
    result=facade.greet(name)

    if len(result)>1:
        return result[1]
    else:
        return ''
    
"""password = 'opensesame'
contents = ': (1) take over the world'
lockbox = LockBox(password, contents)

found_password, found_contents = break_lockbox(lockbox)
print(found_password)
print(found_contents)"""
    
    
    
