#!/usr/bin/env python
# coding: utf-8

# # Funzione di Fibonacci
# 
# ## Obiettivo: 
# 
# Creare una funzione che riceva tramite lo standard input due valori numerici “start” e “steps”. La funzione deve restituire nello standard output un vettore di lunghezza pari a “steps”, il cui primo elemento corrisponda a “start” e ogni valore successivo sia uguale alla somma dei due valori precedenti, emulando la serie di Fibonacci (1,1,2,3,5,8,13,21,…) a partire però dal valore arbitrario “start”.
# 
# Ad esempio se faccio fibonacci(start=2,steps=7) devo ottenere: [2,2,4,6,10,16,26]

# In[91]:


def fibonacci(start,steps):
    if steps<=0:
        print("Steps deve essere maggiore di 0")
        return
    if type(steps)!=type(5):
        print("Steps deve essere un numero intero")
        return
    if type(start)!=type(5) and type(start)!=type(5.2):
        print("Start deve essere numerico")
        return
    if steps==1:
        print([start])
        return
    if steps==2:
        print([start,start])
        return
    risultato=[start,start]
    for j in range(2,steps):
        risultato.append(sum((risultato[j-2],risultato[j-1])))
    print(risultato)


# In[99]:


fibonacci(start=2,steps=7)


# In[ ]:




