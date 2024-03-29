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
# 创建翻译目标并翻译原始单词表
translator = Translator()
russian = translator.translate(english, dest="ru")
russian = str(russian.text)
# 将翻译结果写入txt文件
f = open("russian.txt","w+")
f.writelines(russian)
f.close()
# 在生成的翻译文件每一行开头加入 "-" 
with open('russian.txt', 'r') as f:
    lines = f.readlines()
    lines = ['- ' + line for line in lines]
    with open('russian.txt', 'w') as f:
        f.writelines(lines)
        f.close()
#组合两个语言到一个语言并构建logseq flashcard格式和tagging
with open('english.txt') as f1, open('russian.txt') as f2, open('初来乍到99单词表-english-russian.txt', 'w') as out:
    for line1, line2 in zip(f1, f2):
        print(line1.rstrip(), " #card #english-russian", sep='', file=out)
        out.write('  ')
        out.write(line2)  
#在新文件顶部添加card query信息
cards_query = '## {{cards [[english-russian]]}}\n\n'
with open('初来乍到99单词表-english-russian.txt', 'r+') as file:
   content = file.read()
   file.seek(0)
   file.write(cards_query + content)
   file.close
# 将txt文件转换成markdown文件   
import shutil     
shutil.copyfile("初来乍到99单词表-english-russian.txt", "初来乍到99单词表-english-russian.md")  