import sys
s = ''
s2 = ''
for i in range(1, len(sys.argv)):
    s = s + sys.argv[i] + ' '
s2 = s
print(s2, end=' ')


import sys
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end=' ')

    
import sys
print(' '.join(sys.argv[1:]))
