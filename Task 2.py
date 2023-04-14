from nltk.tokenize import word_tokenize,sent_tokenize 
text = input("Enter some text: ")
print("Choose an option:")
print("1. Print tokenized words")
print("2. Print tokenized sentences")
print("3. Print original text")

choice = int(input('enter number: '))

if choice == 1:
      print(word_tokenize(text))
elif choice == 2:
      print(sent_tokenize(text))
elif choice == 3:
      print(text) 
else:
      print('not found option')
