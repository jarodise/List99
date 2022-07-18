from googletrans import Translator
import shutil
# opening the file in read mode
data = open("list.txt", "r")
# 在每一行开头加入 "-" 
with open('list.txt', 'r') as f:
    english = data.read() # reading the file
    lines = f.readlines()
    lines = ['- ' + line for line in lines]
    with open('english.txt', 'w') as f:
        f.writelines(lines)
        f.close()
print(english)
# 创建翻译目标
translator = Translator()
Turkish = translator.translate(english, dest="tr")
Turkish = str(Turkish.text)
# 将翻译结果写入txt文件
f = open("Turkish.txt","w+")
f.writelines(Turkish)
f.close()
with open('Turkish.txt', 'r') as f:
    lines = f.readlines()
    lines = ['- ' + line for line in lines]
    with open('Turkish.txt', 'w') as f:
        f.writelines(lines)
        f.close()
#组合两个语言到一个语言#
with open('english.txt') as f1, open('Turkish.txt') as f2, open('66单词表-english-Turkish.txt', 'w') as out:
    for line1, line2 in zip(f1, f2):
        print(line1.rstrip(), " #card #english-Turkish", sep='', file=out)
        out.write('  ')
        out.write(line2)  
#在文件顶部添加card query
cards_query = '## {{cards [[english-Turkish]]}}\n\n'

with open('66单词表-english-Turkish.txt', 'r+') as file:
   content = file.read()
   file.seek(0)
   file.write(cards_query + content)
   file.close
# 将txt文件转换成markdown文件   
import shutil     
shutil.copyfile("66单词表-english-Turkish.txt", "66单词表-english-Turkish.md")  