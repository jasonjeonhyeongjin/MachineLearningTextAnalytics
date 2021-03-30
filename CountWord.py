from konlpy.tag import Okt 


# twitter = Okt() 
# print("구분할 문장을 입력해주세요") 
# text = input() 
# #norm은 현대적인말 그래욬ㅋㅋㅋ 같은 것을 그래요로 바꾸어 주는 것이다. 
# # #stem은 그래요를 그렇다처럼 원형으로 바꾸어 주는 것이다. 
# classifiedData = twitter.pos(text,norm=True,stem=True) 
# print(classifiedData)

import codecs 
from bs4 import BeautifulSoup 
text = codecs.open("BEXX0003.txt",'r',encoding = "utf-16") 
bsData = BeautifulSoup(text,'html.parser') 
body = bsData.select_one("body > text") 
text = body.getText() 
twitter = Okt() 
text = text.split('\n') 
dic = {} 
for line in text: 
    malist = twitter.pos(line) 
    for word in malist: 
        if word[1] == "Noun": 
            if word[0] not in dic: 
                dic[word[0]] = 0 
            dic[word[0]]+=1 

sortedDic = sorted(dic.items(), key=lambda k :k[1], reverse=True) 
for word, count in sortedDic[:30]: 
    print("{0}({1})".format(word,count))
