# -*- coding: utf-8 -*-
import random
def chatbot():
	zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]
	reaktionsantworten =   {"hallo": "Hallo du!", 
							"geht": "Was verstehst du darunter?", 
							"essen": "Ich habe leider keinen Geschmackssinn :(",
							"spaß": "Klingt gut!" 
							}
	print("Willkommen beim Chatbot")
	print("Worüber würdest du gerne heute sprechen?")
	print("Zum Beenden einfach 'bye' eintippen")
	print("")
	nutzereingabe = ''
	while nutzereingabe != 'bye':
		nutzereingabe = ''
		while nutzereingabe == '':	
			nutzereingabe = input('Deine Frage/Antwort: ')
		nutzereingabe = nutzereingabe.lower()
		nutzerwoerter = nutzereingabe.split()
		intelligenteAntwort = False
		for einzelwoerter in nutzerwoerter:
			if einzelwoerter in reaktionsantworten:
				print(reaktionsantworten[einzelwoerter])
				intelligenteAntwort = True
		if intelligenteAntwort == False and nutzereingabe != 'bye':
			print(random.choice(zufallsantworten))
		print('')	
	print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal!")
if __name__ == "__chatbot__":
	chatbot()
