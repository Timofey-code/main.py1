newwords = {
            "LOL": "something very funny",
            "CRINGE": "Something very strange or embarrasing",
            "SYFM": "Telling someone to stop talking (quite rude)",
            "HYPE": "Something really cool or exciting",
            "BET": "yes, ok or alright",
            "CAP": "a lie/ not true",
            "DRIP": "stylish, fashionable",
            "SUS": "Suspicious/ suspect",
            "LIT": "exciting/amazing",
            "FLEX": "show off or boast"
            }
word = input("Enter not understood word  (Capital letters!): ")
if word in newwords.keys():
    print(word + " means -> ->  " + newwords[word])
else:
    print(("") + word + ("") + " is not in the meme dictionary")
