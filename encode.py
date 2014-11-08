def encode(message):
    def isTrun(rst):
        if len(rst) < 2:
            return False
        elif rst[0] == 'x':
            return True
        else:
            return '0' <= rst[0] <= '9' and rst[1] == 'x'
            
    rst = ''
    message = ' ' + message
    n = len(message)
    cnt = 0
    prev = None
    for i in range(n - 1, -1, -1):
        if message[i] == prev:
            cnt += 1
        else:
            if cnt > 1:
                rst = str(cnt) + 'x' + prev + rst
            elif prev:
                if isTrun(rst) and '0' <= prev <= '9':
                    rst = '1x' + prev + rst
                else:
                    rst = prev + rst
            cnt = 1
        prev = message[i]
    return rst
print encode('abc673ddddc')
print encode('abc673ddddcabc673ddddc')
print encode('abc5xd')
print encode('abc5xdabc5xd')
print encode('abc673ddddcabc5xd')
print encode('abc5xdabc673ddddc')
