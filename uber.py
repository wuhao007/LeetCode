trigger_time = None
count = 0
count_persecond = 100 / 60 = 1.5
import datatime
def outgoing():
    # make http call to external API
    global trigger, count
    count += 1
    if trigger_time:
        used_time = datetime.datetime.now() - trigger_time   # 60 - 40 = 20
        if used_time < 60 and count > 100:
            while datetime.datetime.now() - trigger_time < 60:
                wait() #O(1) time
            trigger_time = None
#        if used_time * count_persecond < count: # 20 * 1.5 = 30 < count = 40
#            while (datetime.datetime.now() - trigger_time) * count_persecond < count:  # 61..70 - 40 = 30 * 1.5 = 45 > 40
#                wait() #O(1) time
        return response()         
    else:
        trigger_time = datetime.datetime.now()
        count =  1  
  
def call_outgoing():
    outgoing()
    
0                1 
|(1)----i--(99)--|--(100)--i----|
