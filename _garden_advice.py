# garden_advice.py
# Initial version for first upload to GitHub

month = input("Enter the current month: ").strip().lower()
season = input("Enter the current season: ").strip().lower()

# TODO: Move this advice data into functions or dictionaries instead of hardcoding output logic.
# TODO: Add input validation so invalid months and seasons are handled more clearly.
# TODO: Add documentation/comments to explain how the script works.
# TODO: Replace repeated print logic with reusable helper functions.

if month == "january":
    print("January tip: Plan your garden layout and order seeds early.")
elif month == "february":
    print("February tip: Start sowing seeds indoors for spring crops.")
elif month == "march":
    print("March tip: Prepare soil and plant early vegetables.")
elif month == "april":
    print("April tip: Keep weeds under control and water young plants carefully.")
elif month == "may":
    print("May tip: Plant summer vegetables after the last frost.")
elif month == "june":
    print("June tip: Mulch beds to keep moisture in the soil.")
elif month == "july":
    print("July tip: Water deeply during hot weather and harvest regularly.")
elif month == "august":
    print("August tip: Deadhead flowers to encourage more blooms.")
elif month == "september":
    print("September tip: Start planting autumn crops and divide perennials.")
elif month == "october":
    print("October tip: Clear fallen leaves and compost healthy plant waste.")
elif month == "november":
    print("November tip: Protect tender plants from frost.")
elif month == "december":
    print("December tip: Clean and store garden tools for the new year.")
else:
    print("Unknown month entered.")

if season == "spring":
    print("Spring advice: Focus on planting, feeding soil, and managing new growth.")
elif season == "summer":
    print("Summer advice: Water consistently and watch for pests.")
elif season == "autumn":
    print("Autumn advice: Harvest remaining crops and prepare beds for winter.")
elif season == "winter":
    print("Winter advice: Protect plants, plan ahead, and maintain your tools.")
else:
    print("Unknown season entered.")
