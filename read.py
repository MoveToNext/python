fname = raw_input('enter filename:')
print

try:
    fobj = open(fname,'r')
except IOError,e:
    print 'error filename',e
else:
    for each in fobj:
        print each
fobj.close()