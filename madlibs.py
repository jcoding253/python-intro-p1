#Programs String concatenation, combines strings, plugs variables into print lines.


#Function template to input words in CLI for madlib.
def collect_words (type_input, num_words):
    word_list = []

    for i in range(num_words):
        word = input(f"{type_input} {i + 1}: ")
        word_list.append(word)

    return word_list

#List of Functions: array variable = (type of word, number items in array)
adj = collect_words("Adjective", 1)
vb = collect_words("Verb", 4)
vg = collect_words ("-ing Verb", 1)
n = collect_words ("Noun", 2)
an = collect_words("Animal", 2)
p = collect_words ("Person's Name", 4)
l = collect_words ("Place", 2)

#Madlib output story results
madlib = f"I really enjoy {vg[0]}!, it's not everyday that you get to see {p[0]} take on {p[1]} at the edge of the {l[0]}. It's times like these when you really feel {adj[0]} to be alive.\
if I could go back I would {vb[0]} my {n[0]} and {vb[1]} it with {p[2]}'s {an[0]}. Speaking of pet's, I heard {p[3]} is dying to {vb[2]} their {an[1]} at the {l[1]}. This is why I really \
don't {vb[3]} with {n[1]}."

print (madlib)