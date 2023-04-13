from nltk.tokenize import word_tokenize,sent_tokenize 
text = input("Enter some text: ")
print("Choose an option:")
print("1. Print tokenized words")
print("2. Print tokenized sentences")
print("3. Print original text")

choice = int(input('enter number: '))
#NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project
if choice == 1:
      print(word_tokenize(text))
elif choice == 2:
      print(sent_tokenize(text))
elif choice == 3:
      print(text) 
else:
      print('not found option')
