import sys

f = open("toSum.txt","a")
avg = 0.5*(float(sys.argv[1]) + float(sys.argv[2]))
print avg
f.write(str(avg) + "\n")

f.close()
