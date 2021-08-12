import subprocess

#write results in res.txt file
f = open('res_v1.txt', 'w')

#get PASS result: succ = "11 12 22 25 34 64 90"
subprocess.call(["gcc", "succ.c"])
succ = subprocess.check_output(["./a.out"])


#test configurations
#return test=TRUE for PASS
#return test=FALSE for FAIL
def testresult(c):
	#clear patches
	subprocess.call(["cp", "source.c", "succ.c"])

	if 1 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf1.patch"])
		f.write('1 ')
	else:
		f.write('. ')

	if 2 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf2.patch"])
		f.write('2 ')
	else:
		f.write('. ')

	if 3 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf10.patch"])
		f.write('3 ')
	else:
		f.write('. ')

	if 4 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf4.patch"])
		f.write('4 ')
	else:
		f.write('. ')

	if 5 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf5.patch"])
		f.write('5 ')
	else:
		f.write('. ')

	if 6 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf7.patch"])
		f.write('6 ')
	else:
		f.write('. ')

	if 7 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf9.patch"])
		f.write('7 ')
	else:
		f.write('. ')

	if 8 in c:
		subprocess.call(["patch", "succ.c", "-i", "patch/conf8.patch"])
		f.write('8 ')
	else:
		f.write('. ')

	#test result
	subprocess.call(["gcc", "succ.c"])
	result = subprocess.check_output(["./a.out"])
	#print(result)

	test = bool(result == succ)

	print(c)
	if result == succ:
		print("PASS")
		f.write('PASS\n')
	else:
		print("FAIL")
		f.write('FAIL\n')

	#clear patches
	subprocess.call(["cp", "source.c", "succ.c"])

	return test


#delta debugging version 1
#searches a single failure-inducing change 
#without inference
def dd(c):
	c1 = c[:len(c)//2]
	c2 = c[len(c)//2:]

	if len(c) == 1:
		f.write(str(c[0]))
		f.write(' is found\n')
		print(str(c[0]) + " is found")

	elif testresult(c1) == False:
		dd(c1)

	elif testresult(c2) == False:
		dd(c2)


c = [1, 2, 3, 4, 5, 6, 7, 8]

dd(c)

f.close()
