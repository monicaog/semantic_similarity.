import spacy

nlp = spacy.load('en_core_web_md')



#Creates function watch_next - It takes in the description as a parameter and returns the title of the most similar movie.

def watch_next(description):
   file = open("movies.txt", "r")
   file = file.readlines()
   higher_similarity = 0.0
   for token in file:
      title = token [0:7]
      token = nlp(token[9:])
      token2 = nlp (description)
      result = token.similarity(token2)
      if result > higher_similarity:
         higher_similarity = result
         movie_title =  title
   return(movie_title)

description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk 
into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar 
where he is sold into slavery and trained as a gladiator'''

#it calls the function watch_next()
print (f" The title of the most similar movie is {watch_next(description)}")