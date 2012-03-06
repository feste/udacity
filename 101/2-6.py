def find_last(s, t, r=-1):
    next = s.find(t, r+1)
    if next == -1:
        return r
    else:
        return find_last(s,t,next)

print find_last('aaaa', 'a')
        


