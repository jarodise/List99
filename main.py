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
polish = translator.translate(english, dest="pl")
polish = str(polish.text)
# 将翻译结果写入txt文件
f = open("polish.txt","w+")
f.writelines(polish)
f.close()
with open('polish.txt', 'r') as f:
    lines = f.readlines()
    lines = ['- ' + line for line in lines]
    with open('polish.txt', 'w') as f:
        f.writelines(lines)
        f.close()
#组合两个语言到一个语言#
with open('english.txt') as f1, open('polish.txt') as f2, open('初来乍到99单词表-english-polish.txt', 'w') as out:
    for line1, line2 in zip(f1, f2):
        print(line1.rstrip(), " #card #english-polish", sep='', file=out)
        out.write('  ')
        out.write(line2)  
#在文件顶部添加card query
cards_query = '## {{cards [[english-polish]]}}\n\n'

with open('初来乍到99单词表-english-polish.txt', 'r+') as file:
   content = file.read()
   file.seek(0)
   file.write(cards_query + content)
   file.close
# 将txt文件转换成markdown文件   
import shutil     
shutil.copyfile("初来乍到99单词表-english-polish.txt", "初来乍到99单词表-english-polish.md")  