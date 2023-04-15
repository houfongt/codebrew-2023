# Import the Natural Language Toolkit library
import nltk
import json

#################

json_location = "input.json"

f = open(json_location)
items = json.load(f)["food_items"]

#################

# Define the list of synsets to include in the check for food items
included_synsets = ['food', 'fruit', 'confiture']

# Define the list of synsets to exclude from the check for food items
excluded_synsets = ['cup.n.01', 'cup.n.02', 'cup.n.03', 'cup.n.04', 'cup.n.05', 'cup.n.06', 'alcohol.n.01', 'tableware.n.01', 'instrumentality.n.03', 'cut.n.06', 'rack.n.01', 'rack.n.02', 'crockery.n.01', 'natural_object.n.01', 'container.n.01', 'measure.v.03', 'dish.n.02', 'cup.n.06', 'artifact.n.01', 'nutriment.n.01', 'whole.n.02', 'object.n.01', 'physical_entity.n.01', 'entity.n.01', 'fare.n.04', 'cup.n.05']

# Define a function to check if a given synset is a type of food
def test_hypernym(name):
    # Check if the synset is in the excluded synsets list
    if name in excluded_synsets:
        return False
    # Check if the synset starts with 'edible'
    if name.startswith('edible'):
        return True
    # Check if the synset's first part is in the included synsets list
    if name.split(".")[0] in included_synsets:
        return True
    # If none of the above conditions are met, return False
    return False

# Define a function to check if a potential food item is a type of food
def check_individual(potential_food):
    # Use the NLTK WordNet to get the synset (set of synonyms) for the given text
    synsets = nltk.corpus.wordnet.synsets(potential_food)

    # Check if any of the synsets have the food category
    for synset in synsets:

        # Create a list of parent synsets
        parent_list = [synset]

        while len(parent_list) > 0:

            # Get the first synset in the parent list
            parent = parent_list[0]
            parent_list = parent_list[1:]

            # Get the hypernyms of the current synset
            hypernyms = parent.hypernyms()

            # Check if any of the hypernyms are types of food
            for hypernym in hypernyms:
                if test_hypernym(hypernym.name()):
                    return True
                
                # Add any non-excluded hypernyms to the parent list
                for x in hypernyms:
                    if x.name() not in excluded_synsets:
                        parent_list.append(x)

    # If no synset has the food category, return False
    return False

# Define a function to check if a given string is a type of food
def is_food(full_text):
    # Split the text into individual words
    split_text = full_text.split(" ")

    # If the text has more than one word, check each word individually
    if len(split_text) > 1:

        # Check if any individual word is a type of food
        for lexeme in split_text:
            underscored = ""
            underscored += lexeme + "_"
            if check_individual(underscored[:-1]):
                return True

        for lexeme in split_text:
            if not check_individual(lexeme):
                return False

        return True
    
    else:
        return check_individual(full_text)

final_items = []

for value in items:
    if is_food(value):
        final_items.append(value)

#################

final_dict = {"finals":final_items}
json_string = json.dumps(final_dict, separators=(',', ':'))

json_out_location = "array_output.json"

with open(json_out_location, 'w') as f:
    json.dump(json_string, f)

#################
