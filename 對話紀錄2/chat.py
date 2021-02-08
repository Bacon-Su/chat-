def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:#-sig可以去掉記事本的開頭符號
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	n = []
	person = None#宣告person沒有東西
	A_word_count = 0
	V_word_count = 0
	A_sticker_count = 0
	V_sticker_count = 0
	A_imagine_count = 0
	V_imagine_count = 0

	for line in lines:
		s = line.split(' ')#遇到空白就切割,存成清單
		time = s[0]#s[0]是時間
		name = s[1]#s[1]是人名
		chat = s[2:]#從清單s[2]~最後s[n]
		if name == 'Allen':
			if s[2] == '貼圖':
				A_sticker_count += 1
			elif s[2] == '圖片':
				A_imagine_count += 1
			else:
				for m in chat:
					A_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				V_sticker_count += 1
			elif s[2] == '圖片':
				V_imagine_count += 1
			else:
				for m in chat:
					V_word_count += len(m)
	print('Allen傳了', A_sticker_count, '個貼圖')
	print('Allen傳了', A_imagine_count, '張圖片')
	print('Allen傳了', A_word_count, '個字')
	print('Viki傳了', V_sticker_count, '個貼圖')
	print('Viki傳了', V_imagine_count, '張圖片')
	print('Viki傳了', V_word_count, '個字')
	return n

#將轉換完成的對話紀錄寫成output.txt
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()

