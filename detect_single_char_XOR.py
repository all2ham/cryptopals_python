import os
import crypto


f = open(os.path.dirname(__file__) + 'ch4.txt')
found_solns = []
for i, x in enumerate(f):
    bestx = crypto.break_single_byte_cypher(x.rstrip('\n'))
    if len(bestx[1]) > 1:
        found_solns.append(('{0:04f}'.format(bestx[2]), bestx[1]))
        print 'Best match line '+str(i+1), 'with key:' + str(bestx[0]), 'msg: ' +str(bestx[1])

