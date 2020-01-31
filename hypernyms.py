f=open("SimLex999-100.txt","r")
lines=f.readlines()
#lines=str(lines)
result=[]
from nltk import re
lis1=[]
for i in range(0,len(lines)) :
    lis1=lis1+lines[i].split('\t')
lis1
strtry=str(lis1)
strtry=" ".join(re.findall("[a-zA-Z]{2,}", strtry))
#print(strtry)
las=strtry.split(' ')
las
sent1 = list()
sent2 = list()
index = 0
for letter in las:
    if index % 2 != 0:
        sent2.append(letter)
    else:
        sent1.append(letter)
    index += 1
from nltk.corpus import wordnet
syn_name1 = list()
for i in range(0,len(sent1)):
    syn = wordnet.synsets(sent1[i])[0] 
    syn_name1.append(syn.name())
syn_name1
from nltk.corpus import wordnet
syn_name2 = list()
for i in range(0,len(sent2)):
    syn = wordnet.synsets(sent2[i])[0] 
    syn_name2.append(syn.name())
sim=list()
p1=list()
p2=list()
from nltk.corpus import wordnet as wn
for i in range(0,101):
    x=syn_name1[i]
    y=syn_name2[i]
    wd1=wn.synset(x)
    wd2=wn.synset(y)
    sim.append(wd1.path_similarity(wd2))
sim
ind=list()
for i in sim:
    if i is None:
        continue
    else:
        ind.append(sim.index(i))
p1=list()
p2=list()
fsim=list()
for i in ind:
    p1.append(sent1[i])
    p2.append(sent2[i])
    fsim.append(sim[i])
import pandas as pd 
df = pd.DataFrame(list(zip(p1, p2,fsim)), 
               columns =['wd1', 'wd2','fSim']) 
df 
import numpy as np
np.savetxt(r'BioSim-100-predicted.txt.txt',df ,fmt='%s')
import nltk
f1=open("text1.txt",encoding="utf8")
lines=f1.readlines()
lines=str(lines)
import string
lines.translate(str.maketrans('', '', string.punctuation))
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokens=tokenizer.tokenize(lines)
tagged = nltk.pos_tag(tokens)
l1=list()
for i in range(0,len(tagged)):
    if tagged[i][1] == 'NN':
        l1.append(tagged[i])
l1=str(l1)
l1=l1.replace(')',"")
l1=l1.replace('(',"")
l1=l1.replace('NN',"")
w=list()
w=l1.split(" ")
w
p1=('answer','boy','answer','lady','room','thing','boy','state','pair','pride','heart','style','service','pair','perplexed','moment','furniture','time','bed','broom','breath','nothing','cat','beat','boy','door','stood','tomato','garden','voice','angle','distance','noise','time','boy','slack','roundabout','flight','thought','closet','look','mouth','truck','aunt','jam','let','switch','switch')
p1=list(p1)
p2=('air','lady','round','danger','lad','instant','board','fence','aunt','moment','laugh','anything','time','dog','saying','goodness','body','dander','minute','lick','duty','boy','truth','goodness','rod','child','sin','suffering','sister','boy','thing','heart','time','conscience','time','heart','well','man','born','woman','trouble','evening','afternoon','season','vanity','suspicion','evidence','inspiration')
from nltk.corpus import wordnet
syn_name1 = list()
for i in range(0,len(p1)):
    syn = wordnet.synsets(p1[i])[0] 
    syn_name1.append(syn.name())
x1=list()
n=int(len(syn_name1)/2)
for i in range(0,n):
    x1.append(syn_name1[i])
    x2=list()
n=int(len(syn_name1)/2)
for i in range(n,len(syn_name1)):
    x2.append(syn_name1[i])
sim1=list()
from nltk.corpus import wordnet as wn
for i in range(0,n):
    y1=x1[i]
    y2=x2[i]
    wd1=wn.synset(y1)
    wd2=wn.synset(y2)
    sim1.append(wd1.path_similarity(wd2))
sim1 
import pandas as pd 
df = pd.DataFrame(list(zip(p1, p2,sim1)), 
               columns =['wd1', 'wd2','sim']) 
df 
import numpy as np
np.savetxt(r'original-pairs.txt',df ,fmt='%s')
sim1=list()
hyp1=list()
hyp2=list()
from nltk.corpus import wordnet as wn
for i in range(0,n):
    y1=x1[i]
    y2=x2[i]
    wd1=wn.synset(y1)
    wd2=wn.synset(y2)
    hyp1.append(wd1.hypernyms())
    hyp2.append(wd2.hypernyms())
fhyp1=list()
fhyp2=list()
for i in range(0,int(n/2)):
    fhyp1.append(hyp1[i][0])
fhyp2=list()
for i in range(int(n/2),n):
    fhyp2.append(hyp1[i][0])
hl1=list()
hl2=list()
for i in range(0,int(n/2)):
    w1=fhyp1[i]
    w2=fhyp2[i]
    hl1.append(w1.hypernyms())
    hl2.append(w2.hypernyms())
fl=list()
fl1=list()
hypsim=list()
for i in range(0,12):
    fl.append(hl1[i][0])
    fl1.append(hl2[i][0])
for i in range(0,12):
    hp1=fl[i]
    hp2=fl1[i]
    hypsim.append(hp1.path_similarity(hp2))
hypsim
import pandas as pd 
df = pd.DataFrame(list(zip(fl, fl1,hypsim)), 
               columns =['wd1', 'wd2','sim']) 
df 
import numpy as np
np.savetxt(r'original-pairs-hypernyms.txt',df ,fmt='%s')
tl1=("thing","pair","pride","perplexed","bed","nothing","answer","boy","room","beat")
tl2=("instant","aunt","moment","saying","minute","boy","air","lady","lad","goodness")
tsim=["0.125","0.1","0.1","0.1","0.1","0.1","0.09090909090909091","0.08333333333333333","0.08333333333333333","0.08333333333333333"]
import pandas as pd 
df = pd.DataFrame(list(zip(tl1, tl2,tsim)), 
               columns =['wd1', 'wd2','sim']) 
df 
import numpy as np
np.savetxt(r' top.txt',df ,fmt='%s')