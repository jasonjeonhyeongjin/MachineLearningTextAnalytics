
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

#utf-16 인코딩으로 파일열고 글자 출력
fp=codecs.open("BEXX0003.txt", "r",encoding="utf-16")
soup=BeautifulSoup(fp, 'html.parser')
body=soup.select_one("body > text")
text=body.getText()

#텍스트 한줄씩 처리하기
twitter=Okt()
results=[]
lines=text.split("\n")

for line in lines:
    #단어기본형 활용. 형태소 분석
    malist=twitter.pos(line, norm=True, stem=True)
    r=[]
    for (word, pumsa) in malist:
        #어미/조사/구두점 등은 대상에서 제외
        if not pumsa in ["Josa","Eomi","Punctuation"]:
            r.append(word)

    rl=(" ".join(r)).strip() #양쪽 공백 추가하여 조인
    results.append(rl)
    print(rl)

#파일로 출력
with open('toji.wakati','w',encoding='utf-8') as fp:
    fp.write("\n".join(results))
    
#Word2Vec 
data=word2vec.LineSentence('toji.wakati') #텍스트 읽어들이기
model=word2vec.Word2Vec(data,window=10,hs=1,min_count=2,sg=1)
model.save("toji.model")
print("ok")
