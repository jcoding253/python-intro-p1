# Programs String concatenation, combines strings, plugs variables into print lines.

# Function for using iterators to cycle array values.
from itertools import cycle

# Shorthand for each type of word input.
# aj = Adjective
# vb = Verb
# vg = -ing Verb
# no = Noun
# an = Animal
# pn = Person's Name
# lo = Place


# Madlib story plain text, using {} as placeholders for each type of word input, which will turn into iteration input later.
madlib_text= '''
f"I really enjoy {vg}!, it's not everyday that you get to see {pn} take on {pn} at the edge of the {lo}. It's times like these \
when you really feel {aj} to be alive. if I could go back I would {vb} my {no} and {vb} it with {pn}'s {an}. Speaking of pet's, \
I heard {pn} is dying to {vb} their {an} at the {lo}. This is why I really don't {vb} with {no}."
'''


# Function template to count the number of times we call for each type of word input.
def count_occurrences(string, placeholder):
    count = string.count(placeholder)
    return count


# Assigning a count variables to each of the "count_occurrences" functions = (madlib text paragraph, placeholder to be counted)
count_aj = count_occurrences(madlib_text, "{aj}")
count_vb = count_occurrences(madlib_text, "{vb}")
count_vg = count_occurrences(madlib_text, "{vg}")
count_no = count_occurrences(madlib_text, "{no}")
count_an = count_occurrences(madlib_text, "{an}")
count_pn = count_occurrences(madlib_text, "{pn}")
count_lo = count_occurrences(madlib_text, "{lo}")


# Temporary test for counting occurrences (delete me)
print(f"Count of {{vb}}: {count_vb}")


# Function template to input words in CLI for madlib.
def collect_words (type_input, num_words):
    word_list = []

    for i in range(num_words):
        word = input(f"{type_input} {i + 1}: ")
        word_list.append(word)

    return word_list


# Assigning array variables for the "collect_words" array functions = (Prompt text for user CLI, count values)
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


# Initializes an empty string to store the final madlib
madlib_output = madlib_text


# List of placeholders used in the madlib_text, for each type of word, ***must be updated for each type of input from madlib_text***
placeholders = ["{aj}", "{vb}", "{vg}", "{no}", "{an}", "{pn}", "{lo}"]


# Loop through the placeholders and replace them with the corresponding values, ***must be updated for each place holder item***
for placeholder in placeholders:
    if placeholder == "{aj}":
        for i in range(count_aj):
            madlib_output = madlib_output.replace(placeholder, next(aj), 1)  # Replace only one occurrence
    elif placeholder == "{vb}":
        for i in range(count_vb):
            madlib_output = madlib_output.replace(placeholder, next(vb), 1)  # Replace only one occurrence
    elif placeholder == "{vg}":
        for i in range(count_vg):
            madlib_output = madlib_output.replace(placeholder, next(vg), 1)  # Replace only one occurrence
    elif placeholder == "{no}":
        for i in range(count_no):
            madlib_output = madlib_output.replace(placeholder, next(no), 1)  # Replace only one occurrence
    elif placeholder == "{an}":
        for i in range(count_an):
            madlib_output = madlib_output.replace(placeholder, next(an), 1)  # Replace only one occurrence
    elif placeholder == "{pn}":
        for i in range(count_pn):
            madlib_output = madlib_output.replace(placeholder, next(pn), 1)  # Replace only one occurrence
    elif placeholder == "{lo}":
        for i in range(count_lo):
            madlib_output = madlib_output.replace(placeholder, next(lo), 1)  # Replace only one occurrence


# Madlib printing function
print(madlib_output)
