# Meal Magic

## Inspiration
We think it's fair enough to say by now everyone knows food wastage is a recipe for disaster. Despite this, Australians throw away an estimated 7.3 million tonnes of food every year. That's the same as 300 kg per person .... _per year_. This got us thinking about the psychology of food waste. What makes people waste food in the first place?

We decided to share our personal experiences and came to the conclusion that, indeed, food wastage is not because we don't understand its consequences but rather because we don't know what to do with the remaining food items. In particular, students and amateur cooks do not have enough knowledge of what to do with leftover items in their fridge or their pantry. There needed to be a solution that can sustainably utilize these waste items whilst helping a person with no prior culinary knowledge to prepare their next meal.


## What it does
Magic Meal is essentially an image detection web app designed to encourage its users to use leftover food items to make their next meal instead of throwing them away. A user has the option of using their mobile to capture leftover items in their fridge and the AI will detect the food items. Alternatively, they also have the option of manually adding the food items remaining in their fridge. Based on these food items, the app will create a recipe with simple instructions   allowing the user to make their meal instead of throwing away the food items.

## How we built it
For the UI/UX we used Figma to design our app. To complement the theme of sustainability, we chose a light green colour scheme and added a sparkle motif since the app will be using ChatGPT as an API. The app runs using Vue framework and a custom server for the front-end.

For the backend, we first built the vue program running yarn build, and then we uploaded it to a self-hosted web-server running apache2 with nginx as a reverse proxy for added security.
The API scripts for NLTK and GPT were also hosted on the server. 
They were little python programs running as little web-http-servers. They listen to post requests with the JSON data, and then process it, and return it. 

The process goes as follow:
The client using a web browser or webapp requests the pages from the apache2 webserver
the client turns the camera on and posts the image to firebase. Firebase returns a json output of all the elements in the image. 
The client then posts the json of elements to the nltk python webserver, which returns a list of food items. Then, the client can modify and/or add missing foods if necessary. When the client is happy, it posts the list of ingredients to the gpt python webserver. The gpt webserver then sends the request to openai, which returns the recipe, and then passes the recipe onto the client. 

the chatgpt and nltk apis are written in python.

There are separate python programs for the webserver, listening for POST requests and sending back data, and for the openai/ntkl integration.
The python webserver calls the openai/ntkl scripts when it recieves the data.

## Challenges we ran into
From a sales perspective, we needed to identify who exactly is our target audience for Magic Meal (since this app may not seem useful for those who already have well-established culinary knowledge)

One error was that when we were testing the app, the nginx reverse proxy was adding a header of same-origin CORS, which us unable to post the data to a different domain (codebrew.domain vs upload.domain)
To solve this, we modified the reverse proxy paths, who proxy:
/ -> to the apache2 webserver
/upload1 -> to the python apis. 




## Accomplishments that we're proud of
deploy a real-life webserver, with good security practices including https, and certificates.
Create a responsive and nice design with good UI.

## What we learned
How to create a prototype design a web app using Figma, 
Learn the  vue.js framework for creating front-end apps
Learn to use python APIs and apache, and integrate powerful AIs into it.
Learn how to deploy web-apps quickly.




## What's next for Meal Magic 
- Attempting to add additional features for the user to promote sustainable practices (such as providing information on which ingredients and food items are compostable)
- Increasing the amount of recipes that it can provide (using a database?)
- Integrating a database of users and logins, for easy access to past recipes.
- Use a trained AI model to figure out foods close to expiry date, and put a priority to use those foods first. This will greatly enhance the sustainability features of this app.
- deploy the app on the app stores.
