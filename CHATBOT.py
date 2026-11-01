import re

products = {
    "iphone 15": {
        "price": 59999, "rating": 4.5, "reviews": 12500,
        "quality": "Excellent", "availability": "In Stock",
        "price_history": [69999, 64999, 62999, 59999],
        "pros": "Excellent camera, good performance, premium build",
        "cons": "Expensive and no charger included"
    },
    "samsung galaxy s24": {
        "price": 74999, "rating": 4.4, "reviews": 9800,
        "quality": "Excellent", "availability": "In Stock",
        "price_history": [79999, 77999, 74999, 74999],
        "pros": "Excellent display, powerful processor, good camera",
        "cons": "Battery could be better"
    },
    "oneplus 12": {
        "price": 64999, "rating": 4.6, "reviews": 7600,
        "quality": "Excellent", "availability": "In Stock",
        "price_history": [69999, 67999, 65999, 64999],
        "pros": "Fast performance, excellent battery, fast charging",
        "cons": "Camera processing can be improved"
    }
}

intents = {
    "price": ["price", "cost", "how much"],
    "rating": ["rating", "stars"],
    "reviews": ["reviews", "customer reviews"],
    "quality": ["quality", "is it good"],
    "price_history": ["price history", "past price", "price trend"],
    "availability": ["available", "availability", "stock"],
    "pros": ["pros", "advantages", "benefits"],
    "cons": ["cons", "disadvantages", "problems"],
    "recommendation": ["recommend", "should i buy", "worth it"]
}

def preprocess(text):
    return re.sub(r"[^\w\s]", "", text.lower()).split()

def find_product(text):
    text = text.lower()
    for product in products:
        if product in text:
            return product
    return None

def match_intent(text):
    words = preprocess(text)
    for intent, patterns in intents.items():
        for pattern in patterns:
            if all(word in words for word in preprocess(pattern)):
                return intent
    return None

def get_response(intent, product):
    data = products[product]
    name = product.title()

    if intent == "price":
        return f"The current price of {name} is ₹{data['price']}."
    elif intent == "rating":
        return f"{name} has a rating of {data['rating']} out of 5."
    elif intent == "reviews":
        return f"{name} has {data['reviews']} customer reviews."
    elif intent == "quality":
        return f"The quality of {name} is {data['quality']}."
    elif intent == "price_history":
        return "Price history: " + " → ".join(
            f"₹{price}" for price in data["price_history"]
        )
    elif intent == "availability":
        return f"{name} is currently {data['availability']}."
    elif intent == "pros":
        return f"Advantages: {data['pros']}."
    elif intent == "cons":
        return f"Disadvantages: {data['cons']}."
    elif intent == "recommendation":
        if data["rating"] >= 4.5:
            return f"Yes, {name} is worth considering. It has a {data['rating']}/5 rating and {data['quality']} quality."
        return f"{name} can be considered, but compare it with other products before buying."

def chatbot():
    print("\nAvailable Products:")
    for product in products:
        print("-", product.title())

    print("\nAsk about price, rating, reviews, quality, price history, availability, pros, cons, or recommendation.")
    print("Type 'bye' to exit.\n")

    current_product = None

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Happy shopping!")
            break

        product = find_product(user_input)

        if product:
            current_product = product
            print(f"Chatbot: {product.title()} selected. What would you like to know?")
            continue

        intent = match_intent(user_input)

        if current_product is None:
            print("Chatbot: Please enter a product name first.")
        elif intent:
            print("Chatbot:", get_response(intent, current_product))
        else:
            print("Chatbot: I could not understand your query. Ask about price, rating, reviews, quality, price history, availability, pros, or cons.")

chatbot()
