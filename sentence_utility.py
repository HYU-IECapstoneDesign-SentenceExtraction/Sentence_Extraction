# -*- coding: utf-8 -*-
import csv
import re
import numpy as np
def read_damage_csv(directory):
    raw = []
    label_damage = []
    f = open(directory, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        raw.append(line[0])
        label_damage.append(line[1])
    f.close()  
    
    # 빈 text 제거 & 특수문자 제거
    sents = []
    for i in range(len(raw)):
        if(raw[i] != ' '):
            newsent = re.sub('[-=+,#/\?:^$@*\"~&%!<>()"]', '', raw[i])
            sents.append(newsent)
    return sents, label_damage

def token2vec(token_sents, label_damage, word_vectors):
    vec_sents = [] # word embedding 결과
    index = 0
    for token_sent in token_sents:
        temp_sent = []
        for token_word in token_sent:
            # '만조/Noun' 같은 단어가 word_vectors 안에 없는 경우가 있어서
            # 이런 경우에는 단어를 추가하지 않고, 지나가도록 만듦.
            try:
                temp_sent.append(word_vectors.get_vector(token_word))
                              
            except KeyError:# key가 존재하지 않을 때
                pass # 그냥 지나감    
        
        if len(temp_sent) != 0:          
            vec_sents.append(temp_sent)
        else:
            del label_damage[index]
        index = index + 1
            
    empty_index = []
    for i in range(len(vec_sents)):
        if len(vec_sents[i]) == 0:
            print(i)
            empty_index.append(i)
        
    for i in empty_index:
        del vec_sents[i]
        del label_damage[i]

    return vec_sents, label_damage

def zero_padding(sentences):
    new_sentences = []
    zero = np.array([0 for _ in range(100)], dtype=float)

    for sentence in sentences:
        count = 0
        new_sentence = []
        len_sentence = len(sentence)
        while(True):
            if(count<= 50 and count<=len_sentence-1):
                new_sentence.append(sentence[count])
            elif(count<=50 and count>=len_sentence):
                new_sentence.append(zero)
        
            if(len(new_sentence)==50):
                break
        
            count = count+1
        new_sentences.append(new_sentence)
    new_sentences = np.array(new_sentences)
    
    return new_sentences

def circular_padding(sentences):
    new_sentences = []
    for sentence in sentences:
        count = 0
        new_sentence = []
        len_sentence = len(sentence)
        while(True):
            if(count<= 50 and count<=len_sentence-1):
                new_sentence.append(sentence[count])
            elif((count<=50 and count>=len_sentence)):
                while(len(new_sentence)<=50):
                    new_sentence = np.concatenate((new_sentence, sentence), axis=0)
        
            if(len(new_sentence)==50):
                break
            if(len(new_sentence)>50):
                new_sentence = new_sentence[:50]
                break
        
            count = count+1
        new_sentences.append(new_sentence)
    new_sentences = np.array(new_sentences)
    return new_sentences

def reverse_padding(sentences):
    new_sentences = []
    for sentence in sentences:
        count = 0
        new_sentence = []
        len_sentence = len(sentence)
        reverse_sentence = sentences[1][::-1]
        while(True):
            if(count<= 50 and count<=len_sentence-1):
                new_sentence.append(sentence[count])
            elif((count<=50 and count>=len_sentence)):
                while(len(new_sentence)<=50):
                    new_sentence = np.concatenate((new_sentence, reverse_sentence), axis=0)
        
            if(len(new_sentence)==50):
                break
            if(len(new_sentence)>50):
                new_sentence = new_sentence[:50]
                break
        
            count = count+1
        new_sentences.append(new_sentence)
    new_sentences = np.array(new_sentences)
    return new_sentences