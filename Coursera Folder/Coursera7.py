def search(keyword) :
  All_words = []
  for Entry in Thesaurus:
    if keyword == Entry.word:
      for word in Entry.synonyms:
        list_copy = Entry.synonyms.copy()
        All_words= list_copy
        All_words.insert(0,keyword)
  result = 0
  final_result = []
  for search_word in All_words:
    count = 0
    result = 0
    for document in Corpus:
      for word in document:
        if search_word == word:
          count = count + 1
    result = search_word,count
    final_result.append(result)
  return final_result
input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
