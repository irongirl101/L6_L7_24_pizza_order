TOPPINGS = {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}
SIZES = {"S": 8, "M": 10, "L": 12}


def toppings_price(toppings_csv):
    if not isinstance(toppings_csv, str):
        return 0

    total = 0
    for topping in toppings_csv.split(','):
        cleaned = topping.strip().lower()
        if cleaned in TOPPINGS:
            total += TOPPINGS[cleaned]
    return total


def pizza_inches(size):
    if not isinstance(size, str):
        return 0

    normalized = size.strip().upper()
    return SIZES.get(normalized, 0)


def split_bill(text):
    if not isinstance(text, str):
        return 0.0

    try:
        total_str, people_str = text.split('/')
        total = float(total_str.strip())
        people = float(people_str.strip())
    except (ValueError, TypeError):
        return 0.0

    if people == 0:
        return 0.0

    return round(total / people, 2)

def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)
    print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)
    print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)
    print("Per Person:", result)

if __name__ == "__main__":
    main()
