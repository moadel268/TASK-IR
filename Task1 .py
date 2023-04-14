import re
def remove_stop_words(text, stop_words):
    words = text.split()
    filtered_text = " ".join([word for word in words if word.lower() not in stop_words])
    return filtered_text
documents = {
    D1: "new home sales top forecasts",
    D2: "home sales rise in July",
    D3: "increase in home sales in July",
    D4: "July new home sales rise",
}
stop_words = {"in", "is", "a", "and", "are"}
for doc_id, text in documents.items():
    documents[doc_id] = remove_stop_words(text, stop_words)
inverted_index = {}

for doc_id, text in documents.items():
    words = set(re.findall(r'\w+', text.lower()))
    for word in words:
        if word in inverted_index:
            inverted_index[word].add(doc_id)
        else:
            inverted_index[word] = {doc_id}
search_term = input("Enter a word: ").strip().lower()
if search_term in inverted_index:
    print("Output:", ",".join(map(str, sorted(inverted_index[search_term]))))
else:
    print("Output: No matching documents found.")
