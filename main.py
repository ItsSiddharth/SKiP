import pickle
from gensim.models.keyedvectors import KeyedVectors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import argparse
import json
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("word", help = "this is the word you want to skip to")
args = parser.parse_args()

input_word = args.word

filename = 'glove_model.pickle'
infile = open(filename,'rb')
glove_model = pickle.load(infile)
infile.close()


#lis = [['hey',0,1],['matrix', 0, 1],['row', 0 ,1],['matrix',1, 0],['addition',1 ,1],['algebra',1 ,2],['convolution',2,3],['matrix',2 ,3],['google',2,3],['forward',1,4],['matrix',2,3],['is',3,4]] 
with open('data.json') as r:
    dat=json.load(r)

n=(len(dat['results']['items']))
a=dat['results']['items']
l=[]
for i in range(0,n):
    b=[]
    b.append(a[i]["alternatives"][0]["content"])
    try:
        b.append(float(a[i]["start_time"]))
        b.append(float(a[i]["end_time"]))
        l.append(b)
    except:
        continue

#lis = [['hey','0','1'],['matrix', '0', '1'],['row', '0' ,'1'],['matrix','1', '0'],['addition','1' ,'1'],['algebra','1' ,'2'],['convolution','2','3'],['matrix','2' ,'3'],['google','2','3'],['forward','1','4'],['matrix','2','3'],['is','3','4']] 
filtered_list,pos,counter = [],[],[]
distance, count = 0, 0



for word in l:
    example_sent = word[0]
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(example_sent) 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_list.append([w,word[1],word[2]])


for element in filtered_list:
    word = element[0] 
    if word == input_word:
        pos.append(count)
    count = count + 1
for i in range (0,len(pos)-1):
    for j in range (pos[i]+1,pos[i+1]):
        try:
            distance = distance + glove_model.similarity(filtered_list[j][0],input_word)
        except:
            pass
    counter.append(distance/j)
    distance = 0


maximum_value = max(counter)
subprocess.call(['vlc --start-time=' + str(filtered_list[pos[counter.index(maximum_value)]][1]) + ' vh.mp4'],shell =True)

