#Files

fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    t=line.find("0")
    y= float(line[t:])
    count = count + 1
    x= x + y


avg= x/count
print ("Average spam confidence:",avg)