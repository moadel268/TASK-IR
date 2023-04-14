import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

ps = PorterStemmer()
ss = SnowballStemmer("english")

doc=[]
doc.append (input("WRITE YOUR TEXT: "))
choice=int(input(" Choice number 1: Print tokenized words\n Choice number 2: Print tokenized sentences\n Choice number 3: Print original text\n Choice number 4: STEMMING\n CHOOSE THE ACTION YOU WANT: "))

if choice == 1:
    print(nltk.word_tokenize(doc))
elif choice == 2:
    print(nltk.sent_tokenize(doc))
elif choice == 3:
    print(doc)
else:
    choice4=int(input(" Choice 4.1: PORTER STEMMER\n Choice 4.2: SNOWBALL STEMMER\n CHOOSE THE ACTION YOU WANT: "))
    if choice4 == 1:
        for i in doc:
            print (i, ":" , ps.stem(i))
    else:
        for j in doc:
            print (j, ":" , ss.stem(j))
