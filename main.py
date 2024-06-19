from openai import OpenAI
from py_edamam import PyEdamam

temperature = 0.0
def get_completion_from_messages(messages, model = "gpt-3.5-turbo", temperature=temperature):
    response = OpenAI().chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature #degree of randomness
    )
    return response.choices[0].message["conent"]
def nutritional_value(content):    
    # Plug in keys as required
    e = PyEdamam(nutrition_appid='xxx',
            nutrition_appkey='xxx',
            recipes_appid='xxx',
            recipes_appkey='xxx',
            food_appid= content,
            food_appkey='xxx')

    for recipe in e.search_recipe("onion and chicken"):
        print(recipe)
        print(recipe.calories)
        print(recipe.cautions, recipe.dietLabels, recipe.healthLabels)
        print(recipe.url)
        print(recipe.ingredient_quantities)
        break

    for nutrient_data in e.search_nutrient("2 egg whites"):
        print(nutrient_data)
        print(nutrient_data.calories)
        print(nutrient_data.cautions, nutrient_data.dietLabels,
            nutrient_data.healthLabels)
        print(nutrient_data.totalNutrients)
        print(nutrient_data.totalDaily)

    for food in e.search_food("coffee and pizza"):
        print(food)
        print(food.category)
        
        
messages = [
{'role':'system','content': 'You are a instagram content creator who likes to explore the world \
                                and the fantasy world too, including but not limited to anime, cartoons, \
                                etc. You will generate 1 recipe that is popular with emojis that are less\
                                that 300 characters long from a different universe each time.'},
{'role':'user','content': 'I want to create content on balanced tasty diets.'}
]

# Vary the temperature
temperatures = [0, 0.2, 0.5, 0.8, 1]
for temperature in temperatures:
    print(temperature)
    content = get_completion_from_messages(messages=messages, temperature=temperature)
    print(content)
    nutritional_value(content)
    
