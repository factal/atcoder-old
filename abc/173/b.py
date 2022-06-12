ac = 0
wa = 0
tle = 0
re = 0

n = int(input())
for i in range(n):
    testcase = input()
    if testcase == 'AC':
        ac += 1
    elif testcase == 'WA':
        wa += 1
    elif testcase == 'TLE':
        tle += 1
    elif testcase == 'RE':
        re += 1

print('AC x', ac)
print('WA x', wa)
print('TLE x', tle)
print('RE x', re)