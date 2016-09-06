import sys

if len(sys.argv) != 2:
    print "Must have a single argument that is an unformatted json file."
else:
    with open(sys.argv[1], 'r') as f:
        txt = f.read()
        txt = txt.replace('}\n{', '},{')[:-1]
    with open(sys.argv[1] + '_new.txt', 'w') as f2:
        f2.write('[')
        f2.write(txt + ']')
