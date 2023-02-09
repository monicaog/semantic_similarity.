import spacy

nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("dog")
word5 = nlp("bone")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word5))
print(word4.similarity(word1),end = "\n\n")

'''
Even though, in life we make associations, like a banana with a monkey, they belong to different categories, fruits and animals, therefore
there is more similarity between animals (cat and monkey), than our preconceived idea of a monkey eating a banana.
One similar example is dog and bone, and dog and cat.
'''

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\n\n")


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

