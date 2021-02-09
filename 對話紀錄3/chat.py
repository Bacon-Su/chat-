lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	print(s)
	time = s[0][:5]#分割s[0]字串(字串也是清單),01234
	name = s[0][5:]#5~最後
	print(name)
	print(time)