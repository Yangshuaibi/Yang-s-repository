from sys import argv

from os.path import exists


script, from_file, to_file = argv


print "Copying from %s to %s" % (from_file, to_file)


input = open(from_file)

indata = input.read()





output = open(to_file,'w')

output.write(indata)

print "Alright, all done."


output.close()

input.close()
