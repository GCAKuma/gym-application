def bmical(w, h):
    bmi=w / (h * h)
    return bmi

def intbmi(bmi, h):
    if bmi < 18.5:
        lb = 18.5 - bmi
        x = lb * (h * h)
        return f"Underweight\nYou have to increase your weight by at least {x} kg"
    elif bmi < 24.5:
        return "Normal"
    else:
        hb = bmi - 24.5
        x = hb * (h * h)
        return f"Overweight\nYou have to decrease your weight by at least {x} kg"

details_dict = {}

n = "y"
while n.lower() == "y":
    name = input("Enter your name: ")
    weight = float(input(f"Enter weight for {name} (kg): "))
    height = float(input(f"Enter height for {name} (m): "))
    calculated_bmi = bmical(weight, height)
    condition = intbmi(calculated_bmi, height)
    details_dict[name] = {
        "Weight": weight,
        "Height": height,
        "BMI": calculated_bmi,
        "Condition": condition,
    }
    n = input("---Are there another student (y/n)---")

# Function to search for a name and retrieve details
def search_name(name):
    if name in details_dict:
        return details_dict[name]
    else:
        return "Name not found in the details."

# Multiple searches or file saving based on user choice
while True:
    user_choice = input("********Menu(Press number)*********\n1. Enter 'Name' for search\n2. To save details to a file\n>>Enter your response: ")

    if user_choice == '1':
        while True:  # Loop for continuous name searches until user exits
            name_to_search = input("Enter a name to search for (press 'q' to quit searching): ")
            if name_to_search.lower() == 'q':
                break  # Break out of the name search loop
            result = search_name(name_to_search)

            if isinstance(result, dict):
                print("_____________________________________________")
                print(f"Details for {name_to_search}:")
                for key, value in result.items():
                    print(f"{key}: {value}")
                print("_____________________________________________")
            else:
                print(result)

    elif user_choice == '2':
        # Writing details to a text file
        with open("all_details.txt", "w") as file:
            for name, details in details_dict.items():
                file.write(f"Name: {name}\n")
                for key, value in details.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
        print("All details have been saved to 'all_details.txt'")
        break

    elif user_choice.lower() == 'q':
        break

    else:
        print("Invalid choice. Please enter 1 or 2.")



