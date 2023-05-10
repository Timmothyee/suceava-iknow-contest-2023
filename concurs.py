import re

#deschide fisierul cu text
f = open('Text.txt','r') 
text = f.read()

list1 = ["artificial", 3.14, "intelligence", 42, "machine", -10, "learning", 7.5, "neural", 0.01, "network", 987, "algorithm", 2, "data", 55, "analytics", -3.33, "chatbot", 99, "voice", -10.5, "recognition", 6, "image", 20, "processing", 0.5, "natural", 12345, "language", 8.88, "generation", 30, "deep", 500, "reinforcement", 0.1, "unsupervised", 999]
list2 = ["deep", 2.718, "learning", 42, "artificial", -10, "intelligence", 7.5, "neural", 1234, "network", 0.01, "computer", 987, "vision", 2, "natural", 55, "language", -3.33, "speech", 99, "recognition", -10.5, "generative", 6, "adversarial", 20, "reinforcement", 0.5, "algorithm", 1000, "big", 8.88, "data", 30, "decision", 500, "trees", 0.1, "unsupervised", 999]
list3 = list1 + list2
caractere_speciale = """., []{}()/"'"""
cuvinte = ['AI', 'military', 'technology', 'development']


def lowestNumber(in_str):
    l=[int(x) for x in in_str.split() if x.isdigit()]
    return min(l) if l else None

def largestNumber(in_str):
    l=[int(x) for x in in_str.split() if x.isdigit()]
    return max(l) if l else None

def numberSum(in_str):
    l=[int(x) for x in in_str.split() if x.isdigit()]
    suma = 0
    for number in l:
        suma = suma + number
    return suma

# Decodes roman numerals
def get_arabic_numbers(t):
    # Hold the numbers in the list
    l = list()

    # The format
    format = 0

    # Convert from roman numeral to arabic number
    ROMAN_TO_INT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in t:
        l.append(ROMAN_TO_INT[i])

    # Calculate the format as follows:
    i = 0
    while i < len(l) - 1:
        # If the next numeral is greater than the current one, add the next one minus the current one = format = format + next_numeral - current_numeral
        if l[i] < l[i+1]:
            format = format + l[i+1] - l[i];
            i = i + 2
        # Else add it normally
        else:
            format = format + l[i]
            i = i + 1

    # Fix in case the last two numerals are equal
    if i == len(l):
        if l[i-2] == l[i-1]:
            format = format + l[i-1]
    else:
        format = format + l[i]

    # Return the format
    return format




#Numarul de litere
nrlitere=0
for litere in text:
    if litere not in caractere_speciale:
        nrlitere = nrlitere + 1
print('Numarul de litere din text e ',nrlitere)


#imparte textul in cuvinte fara caractere speciale in afara de \n
textsplit = re.split(r"[ ,.!?()]",text) 

#sterge caracterele nefolositoare
try:
    for i in textsplit:
        if(i==''):
            textsplit.remove('')
except:
    pass


#numara cate cuvinte sunt
word_count = 0
for i in textsplit:
    word_count = word_count + 1
print('Numarul de cuvinte din text e: ', word_count)



#De cate ori apare a

word_count = 0
number_a = 0


for i in text:
    if i == 'a' or i == 'A':
        number_a = number_a + 1
    if i not in caractere_speciale:
        word_count = word_count + 1

print('Litera a apare de ',number_a,' ori')

textsplit = re.split(r"\W+",text) 
#verifica de cate ori apar cuvintele date
nrcuv = 0
for i in textsplit:
    if i in cuvinte:
        nrcuv = nrcuv + 1
print('Cuvintele AI, military, technology, development, apar in text de ',nrcuv, ' ori')


#Propozitia cu toate literele din alfabet

import string
 
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

p = ""
split=re.split(r'[.]',text)

for i in split:
    if(ispangram(i) == True):
        p=i
    else:
        pass
print('Propozitia cu toate literele din alfabet din text e ',p)

#Nu e cea mai eficienta metoda, dar vede cel mai folosit cuvant din text
count=0
maxCount=0
for i in range(0, len(textsplit)):  
    count = 1;  
    #Count each word in the file and store it in variable count  
    for j in range(i+1, len(textsplit)):  
        if(textsplit[i] == textsplit[j]):  
            count = count + 1; 
    if(count > maxCount):  
        maxCount = count;  
        word = textsplit[i];  
print('Cel mai folosit cuvant din text e ',word)


#pozitia cuvantului champions
print('Cuvantul champions apare pe pozitia ',text.find('champions'))

#cel mai lung cuvant din text
wordsList = text.split()
longestWordLength = len(max(wordsList, key=len))
result = [textword for textword in wordsList if len(textword) == longestWordLength]
print(result)

#numarul maxim din text
print('Cel mai mare numar din text e ',largestNumber(text))

#numarul minim din text
print('Cel mai mic numar din text e ',lowestNumber(text))

#Rezultatul adunarii numerelor din text
print('Rezultatul adunarii numerelor din text e ',numberSum(text))



# Decodes roman numerals
def get_arabic_numbers(t):
    # Hold the numbers in the list
    l = list()

    # The format
    format = 0

    # Convert from roman numeral to arabic number
    ROMAN_TO_INT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in t:
        l.append(ROMAN_TO_INT[i])

    # Calculate the format as follows:
    i = 0
    while i < len(l) - 1:
        # If the next numeral is greater than the current one, add the next one minus the current one = format = format + next_numeral - current_numeral
        if l[i] < l[i+1]:
            format = format + l[i+1] - l[i];
            i = i + 2
        # Else add it normally
        else:
            format = format + l[i]
            i = i + 1

    # Fix in case the last two numerals are equal
    if i == len(l):
        if l[i-2] == l[i-1]:
            format = format + l[i-1]
    else:
        format = format + l[i]

    # Return the format
    return format

#Convertirea din roman in arabic
print(get_arabic_numbers('MMMCMXCIX'))

#creeaza o lista noua care contine doar numere
new_list = [i for i in list3 if isinstance(i,int)==True or isinstance(i,float)==True]

#numarul maxim din lista3
print('Numarul cel mai mare din lista3 e ',max(new_list))
#numarul minim din lista 3
print('Numarul cel mai mic din lista3 e ',min(new_list))
print('Numerele din lista3 sunt: ',new_list)

#creeaza o lista noua care contine doar cuvinte
new_list = [i for i in list3 if isinstance(i,str)==True]
print('Cuvintele din lista3 sunt: ',new_list)

print('Elementele unice din lista3 sunt: ',set(list3))


seen = set()
dupes = []

#daca au fost gasite deja, atunci le adauga la lista
for x in list3:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)
print('Elementele duplicate din lista3 sunt: ',dupes)

list1.reverse()
print('Lista1 reversata este: ',list1)


