def mid(txt,start,le=1):
    s=txt[start:start+le]
    return s
s='Excel与Python'
print(mid(s,3,5))
print(mid(le=5,start=3,txt=s))
print(mid(s,3,le=5))
