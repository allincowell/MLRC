import os
import shutil

rootdir="."

for entry in os.listdir(rootdir):
	f=os.path.join(rootdir, entry)
	if os.path.isfile(f):
		continue
	for entry2 in os.listdir(f):
		path=os.path.join(rootdir, entry2)
		os.mkdir(path)
		f2=os.path.join(f, entry2)
		if os.path.isfile(f2):
			continue
		for entry3 in os.listdir(f2):
			f3=os.path.join(f2, entry3)
			if f3.endswith(".csv"):
				print(entry, entry2, entry3)
				print(f, f2, f3)
				shutil.copy(f3, path)