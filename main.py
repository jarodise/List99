from googletrans import Translator
import shutil
# opening the file in read mode
data = open("list.txt", "r")
# 在每一行开头加入 "-" 
with open('list.txt', 'r') as f:
    english = data.read() # reading the file
    lines = f.readlines()
    lines = ['- ' + line for line in lines]
    with open('en.txt', 'w') as f:
        f.writelines(lines)
        f.close()
print(english)
# 创建翻译目标
translator = Translator()
turkish = translator.translate(english, dest="tr")
turkish = str(turkish.text)
# 将翻译结果写入txt文件
f = open("tr.txt","w+")
f.writelines(turkish)
f.close()
with open('tr.txt', 'r') as f:
    lines = f.readlines()
    lines = ['- ' + line for line in lines]
    with open('tr.txt', 'w') as f:
        f.writelines(lines)
        f.close()
print(turkish)
#组合两个语言到一个语言#
with open('en.txt') as f1, open('tr.txt') as f2, open('en-tr.txt', 'w') as out:
    for line1, line2 in zip(f1, f2):
        print(line1.rstrip(), " #card #en-tr", sep='', file=out)
        out.write('  ')
        out.write(line2)  
#在文件顶部添加card query
cards_query = '## {{cards [[en-tr]]}}\n\n'

with open('en-tr.txt', 'r+') as file:
   content = file.read()
   file.seek(0)
   file.write(cards_query + content)
   file.close
# 将txt文件转换成markdown文件   
import shutil     
shutil.copyfile("en-tr.txt", "en-tr.md")  