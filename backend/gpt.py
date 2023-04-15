# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import json

# Key will be on the server only
openai.api_key = "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"

#################

json_location = "input_gpt.json"

f = open(json_location)
final_items = json.load(f)["food_items"]

#################

# In case user has given no items
if len(final_items) <= 0:
    final_recipe = "No ingredients! Add some ingredients by using the in-built camera, or type them in yourself."

# Normal use case
else:
    prompt = ""

    # Define the prompt engineering text for the recipe request
    prompt_engineering = "I have the following items in my fridge/cupboard, and I would like to make a meal, \
    so they do not go to waste. Write me a simple recipe with only these ingredients so that I can use them \
    up (you do not have to use all the ingredients, but the more you use the better). Only write one recipe. \
    Do not include anything else, as I cannot go to the shops, but you can assume I have access to basic \
    condiments such as salt, pepper, etc. Make sure the title of the meal is in bold text. Make sure \
    if the food is edible and can make a tasty meal with conventional flavour combinations. Ingredients: "

    prompt += prompt_engineering

    for food in final_items:
        prompt += str(food) + ", "

    prompt = prompt[:-2]

    # Model Engine Detail
    model_engine = "text-davinci-003"

    # Set the maximum number of tokens to generate in the response
    max_tokens = 1000

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    final_recipe = completion.choices[0].text.strip()

js_style_recipe = final_recipe.replace('\n', '</br>')

#################

final_dict = {"recipe":js_style_recipe}
json_string = json.dumps(final_dict, separators=(',', ':'))

json_out_location = "recipe_output.json"

with open(json_out_location, 'w') as f:
    json.dump(json_string, f)

#################
