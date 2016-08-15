'''
// This is the text editor interface. 
// Anything you type or change here will be seen by the other person in real time.

// function log parsing

// env is a single thread/single cpu
// input:
// name(string), is_start(boolean), timestamp(long)
// f1, start, 0
// f2, start, 1
// f1, start, 3
// f1, end, 7
// f2, end, 10
// f1, end, 14
// f3, start, 20
// f3, end, 21

// output:
f1: [0, 1], [3, 7], [10, 14]
f2: [1, 3], [7, 10]
f3: [20, 21]
'''

def process(logs):
    stack = []
    res = {}
    for i in range(1, len(logs)):
        if logs[i-1].is_start and logs[i].is_start:
            res[logs[i-1].name] = res.get(logs[i-1].name, []) + [(logs[i-1].timestamp, logs[i].timestamp)]
        elif logs[i-1].is_start and not logs[i].is_start:
            res[logs[i-1].name] = res.get(logs[i-1].name, []) + [(logs[i-1].timestamp, logs[i].timestamp)]
        elif not logs[i-1].is_start and logs[i].is_start:
            continue
        elif not logs[i-1].is_start and not logs[i].is_start:
            res[logs[i].name] = res.get(logs[i].name, []) + [(logs[i-1].timestamp, logs[i].timestamp)]
        '''
        if len(stack) == 0:
            stack.append(log)
        else:
            if stack[-1].name == log.name and stack[-1].is_start and not log.is_start:
                res[log.name] = res.get(log.name, []) + [(stack[-1].timestamp, log.timestamp)]
                stack.pop()
            else:
                stack.append(log)
        '''
            
    return res

class Log():
    def __init__(self, name, start, timestamp):
        self.name = name
        self.is_start = start
        self.timestamp = timestamp
'''
// f1, start, 0
// f1, start, 1
// f1, start, 3
// f1, end, 7
// f1, end, 10
// f1, end, 14
// f1, start, 20
// f1, end, 21
'''
logs = [Log("f1", True, 0), 
        Log("f2", True, 1),
        Log("f1", True, 3),
        Log("f1", False, 7),
        Log("f2", False, 10), 
        Log("f1", False, 14),
        Log("f3", True, 20),
        Log("f3", False, 21)]
print process(logs)
logs = [Log("f1", True, 0), 
        Log("f1", True, 1),
        Log("f1", True, 3),
        Log("f1", False, 7),
        Log("f1", False, 10), 
        Log("f1", False, 14),
        Log("f1", True, 20),
        Log("f1", False, 21)]
#[0, 14], [20, 21]
print process(logs)

#stack = [f1, f2, f1]
