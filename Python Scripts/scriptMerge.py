import glob
from pathlib import Path
filenames = glob.glob(r'E:/MCA/2nd Sem/DS/DS Lab/Assignment/*.cpp')
#filenames = ['0.cpp', '1.cpp', '2.cpp', '3.cpp']
outfile = open('Assignment.txt', 'w', encoding = "UTF-8")
i = 1
for fname in filenames:
	with open(fname) as infile:
		outfile.write('Question %d\n' % i)
		for line in infile:
			outfile.write(line)
		outfile.write("\n___________________________________________________________________________\n")
		i = i + 1
print("Successful!")
outfile.close()
