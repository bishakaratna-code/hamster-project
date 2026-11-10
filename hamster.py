import requests
import random
import pyperclip

# List of kawaii emotes!!!
hamsters = [
    "ʕ•ᴥ•ʔ",
    "૮₍ ´ ꒳ `₎ა",
    "(｡•́‿•̀｡)",
    "ᘛ⁐̤ᕐᐷ",
    "(づ｡◕‿‿◕｡)づ",
    "૮₍ ˶• ༝ •˶ ₎ა",
    "(๑•́ ₃ •̀๑)"
]

#Wiki url and parameters for the API request to get hamster facts
url = "https://en.wikipedia.org/w/api.php"

#Wiki params to get a random hamster fact from the "Hamster" page 
#Change titles to get a random fact from a different page
#Change key based on print(facts["query"]["pages"].keys()) to the page ID of the page you want to get a random fact from
params = {
    "action": "query",
    "prop": "extracts",
    "titles": "Hamster",
    "explaintext": 1,
    "format": "json",
    "exsectionformat": "plain"
}

#The API request to get hamster facts
response = requests.get(
    url,
    params=params,
    headers={"User-Agent": "HamsterLearningProject/1.0 (educational Python project)"},
    timeout=10
)
print(response.status_code)

#String modification stuff to get a random hamster fact from the API response
facts = response.json()
print(facts["query"]["pages"].keys())
quote = facts["query"]["pages"]["14376"]["extract"]
fact = quote.split(". ")

print("Number of facts:", len(fact))
print("First fact:", repr(fact[0]))

pick = random.choice(fact)
fin = pick.replace("\n", "")

note = "Random Hamster Fact: " + fin
hamster = random.choice(hamsters)

pyperclip.copy(note + " " + hamster)

print("Successfully copied to clipboard: " + note + " " + hamster)