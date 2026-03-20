"""Provide gardening advice based on the month and season.

This script asks the user for a month and season, validates the input,
and then prints gardening tips for each.
"""

# Advice is stored in dictionaries to avoid hardcoded output logic in condition chains.
MONTH_ADVICE = {
    "january": "Plan your garden layout and order seeds early.",
    "february": "Start sowing seeds indoors for spring crops.",
    "march": "Prepare soil and plant early vegetables.",
    "april": "Keep weeds under control and water young plants carefully.",
    "may": "Plant summer vegetables after the last frost.",
    "june": "Mulch beds to keep moisture in the soil.",
    "july": "Water deeply during hot weather and harvest regularly.",
    "august": "Deadhead flowers to encourage more blooms.",
    "september": "Start planting autumn crops and divide perennials.",
    "october": "Clear fallen leaves and compost healthy plant waste.",
    "november": "Protect tender plants from frost.",
    "december": "Clean and store garden tools for the new year.",
}

SEASON_ADVICE = {
    "spring": "Focus on planting, feeding soil, and managing new growth.",
    "summer": "Water consistently and watch for pests.",
    "autumn": "Harvest remaining crops and prepare beds for winter.",
    "winter": "Protect plants, plan ahead, and maintain your tools.",
}


def normalise_user_input(prompt):
    """Return cleaned user input in lowercase."""
    return input(prompt).strip().lower()



def get_advice(user_value, advice_map, label):
    """Return formatted advice text for a validated month or season."""
    if user_value not in advice_map:
        valid_options = ", ".join(advice_map.keys())
        return f"Invalid {label}. Please choose one of: {valid_options}."
    return f"{label.title()} advice: {advice_map[user_value]}"



def main():
    """Run the gardening advice application."""
    month = normalise_user_input("Enter the current month: ")
    season = normalise_user_input("Enter the current season: ")

    print(get_advice(month, MONTH_ADVICE, "month"))
    print(get_advice(season, SEASON_ADVICE, "season"))


if __name__ == "__main__":
    main()
