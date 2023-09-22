# Programs String concatenation, combines strings, plugs variables into print lines.

# Function for using iterators to cycle array values.
from itertools import cycle

# Variable iterators for each type of word inputted.
# aj = Adjective
# vb = Verb
# vg = -ing Verb
# no = Noun
# an = Animal
# pn = Person's Name
# lo = Place


# Madlib output story text, using {{ }} to treat the iterator variables as plain text, so they aren't called upon and trigger an error.

madlib_text= '''
f"I really enjoy {{next(vg)}}!, it's not everyday that you get to see {{next(pn)}} take on {{next(pn)}} at the edge of the {{next(lo)}}. It's times like these \
when you really feel {{next(aj)}} to be alive. if I could go back I would {{next(vb)}} my {{next(no)}} and {{next(vb)}} it with {{next(pn)}}'s {{next(an)}}. Speaking of pet's, \
I heard {{next(pn)}} is dying to {{next(vb)}} their {{next(an)}} at the {{next(lo)}}. This is why I really 
don't {{next(vb)}} with {{next(no)}}."
'''

# Function template to count the number of times we call for each type of variable.
def count_occurrences(string, placeholder):
    count = string.count(placeholder)
    return count

# Assigning a count variables to each of the "count_occurrences" functions = (string text paragraph, string text segment to be counted)
count_aj = count_occurrences(madlib_text, "{next(aj)}")
count_vb = count_occurrences(madlib_text, "{next(vb)}")
count_vg = count_occurrences(madlib_text, "{next(vg)}")
count_no = count_occurrences(madlib_text, "{next(no)}")
count_an = count_occurrences(madlib_text, "{next(an)}")
count_pn = count_occurrences(madlib_text, "{next(pn)}")
count_lo = count_occurrences(madlib_text, "{next(lo)}")


# Temporary test for counting occurrences (delete me)
print(f"Count of {{next(vb)}}: {count_vb}")

    
# Function template to input words in CLI for madlib.
def collect_words (type_input, num_words):
    word_list = []

    for i in range(num_words):
        word = input(f"{type_input} {i + 1}: ")
        word_list.append(word)

    return word_list

# Assigning array variables for the "collect_words" array functions = (type of word, count values)
aj_arr = collect_words("Adjective", count_aj)
vb_arr = collect_words("Verb", count_vb)
vg_arr = collect_words("-ing Verb", count_vg)
no_arr = collect_words("Noun", count_no)
an_arr = collect_words("Animal", count_an)
pn_arr = collect_words("Person's Name", count_pn)
lo_arr = collect_words("Place", count_lo)


# Create iterators for each array
aj = cycle(aj_arr)
vb = cycle(vb_arr)
vg = cycle(vg_arr)
no = cycle(no_arr)
an = cycle(an_arr)
pn = cycle(pn_arr)
lo = cycle(lo_arr)


# Madlib output text, filled in with user inputs.
madlib_output = f"I really enjoy {next(vg)}!, it's not everyday that you get to see {next(pn)} take on {next(pn)} at the edge of the {next(lo)}. It's times like these \
when you really feel {next(aj)} to be alive. if I could go back I would {next(vb)} my {next(no)} and {next(vb)} it with {next(pn)}'s {next(an)}. Speaking of pet's, \
I heard {next(pn)} is dying to {next(vb)} their {next(an)} at the {next(lo)}. This is why I really don't {next(vb)} with {next(no)}."


#Madlib printing function
print (madlib_output)