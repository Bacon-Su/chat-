def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:#-sig可以去掉記事本的開頭符號
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None#宣告person沒有東西
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:#如果person有值
			new.append(person + ': ' + line)
	return new

#將轉換完成的對話紀錄寫成output.txt
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()