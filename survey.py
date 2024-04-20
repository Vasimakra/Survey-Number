# Sample data representing districts, mandals, villages, and survey numbers
data = {
    "District1": {
        "Mandal1": {
            "Village1": ["Survey1", "Survey2", "Survey3"],
            "Village2": ["Survey4", "Survey5"]
        },
        "Mandal2":{
            "Village3": ["Survey6", "Survey7"],
            "Village4": ["Survey8", "Survey9", "Survey10"]
        },
        "Mandal3": {
            "Village5": ["Survey11", "Survey12"],
            "Village6": ["Survey13", "Survey14", "Survey15"]
        }
    },
    "District2": {
        "Mandal4": {
            "Village7": ["Survey16", "Survey17"],
            "Village8": ["Survey18"]
        },
        "Mandal5": {
            "Village7": ["Survey19", "Survey20"],
            "Village8": ["Survey21", "Survey22", "Survey23"]
        }
    }
}

def get_survey_numbers(district, mandal, village):
    if district in data and mandal in data[district] and village in data[district][mandal]:
        return data[district][mandal][village]
    else:
        return []

# Read inputs from standard input
district = input("Enter district: ")
mandal = input("Enter mandal: ")
village = input("Enter village: ")

survey_numbers = get_survey_numbers(district, mandal, village)
if survey_numbers:
    print("Survey numbers for {}, {}, {}: {}".format(district, mandal, village, ", ".join(survey_numbers)))
else:
    print("No survey numbers found for {}, {}, {}".format(district, mandal, village))
