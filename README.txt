succ.c: successful version
fail.c: fail version

patch folder contains 10 patches (manually generated) for changes. 
patch 1-8 are changes for version 2 which search two failure-inducing changes with interference.
patch 1,2,4,5,7,8,9,10 are changes for version 1 which search single failure-inducing changes.

test case
The succ.c performs a successful bubble sort on a ginven array. By adding some changes, fail.c fails the correct bubble sort. The output of fail.c is wrong.
My test is made by comparing the output of patched file with the output of succ.c. If the output is the same as the successful output, the test will succeed (PASS). Otherwise, the output is different from successful output, the test will fail (FAIL).

dd_v1.py
Version 1 of delta debugging searches a single failure-inducing change without inference.
I make the performance the same as the example of Table 1. Change 7 is the one that causes the failure, which is the patch 9.
dd(c) = c	if|c|=1 ("found")
	dd(c1)	else if test(c1)=FAIL ("in c1")
	dd(c2)	else if test(c2)=FAIL ("in c2")
The result of dd_v1 is written in text file res_v1.txt
1 2 3 4 . . . . PASS
. . . . 5 6 7 8 FAIL
. . . . 5 6 . . PASS
. . . . . . 7 8 FAIL
. . . . . . 7 . FAIL
7 is found

dd_v2.py (Algorithm 1)
Version 2 of delta debugging searches two failure-inducing changes with inference.
I make the performance the same as the example of Table 2. Change 3 and 6 are the changes that causes the failure, which are the patch 3 and 6.
dd(c, r) = c				if|c|=1 ("found")
	dd(c1, r)			else if test(c1)=FAIL ("in c1")
	dd(c2, r)			else if test(c2)=FAIL ("in c2")
	dd(c1, c2 U r) U dd(c2, c1 U r) otherwise ("interference")
The result of dd_v2 is written in text file res_v2.txt
1 2 3 4 . . . . PASS
. . . . 5 6 7 8 PASS
1 2 . . 5 6 7 8 PASS
. . 3 4 5 6 7 8 FAIL
. . 3 . 5 6 7 8 FAIL
3 is found
1 2 3 4 5 6 . . FAIL
1 2 3 4 5 . . . PASS
1 2 3 4 . 6 . . FAIL
6 is found

How to run:
For dd_v1, run command:
python dd_v1.py
For dd_v2, run command:
python dd_v2.py

Findings and Thoughs:
1. Applying algorithm 1 in one step was a little bit hard for me. Thus, I tried to divide into two steps. At first, the simple delta debugging as example 1 without interference. Then, add interference to complete algorithm 1 as example 2.\
2. At the beginning of the project, I tried to find a way to run command and get the result. I found subprocess in Python. Therefore, I used Python for this project. I'm willing to learn how to do this in C.
subprocess.call: run command
subprocess.check_output: get command calling result
3. If two changes were in continuous lines, there was Hunk fail issue. To avoid it, I applied changes in not continuous lines.
4. After every time appling patches and finishing test, it's necessary to reverse patches. I tried the command line of reversing patches. However, it worked in command but I did not find a way to perform '<' or '>' in Python subprocess.call. So I tried to clear patches applied to succ.c by copying succ.c from source.c.
5. For the test, I applied the test by comparing result with correct result. If the result is different from correct one, I thought the test fail.
