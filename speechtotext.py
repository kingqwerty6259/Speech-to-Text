import speech_recognition as sr

r = sr.Recognizer()

while True:
	try:
		with sr.Microphone() as source:
			print("Connected")
			audio = r.listen(source)
			text = r.recognize_google(audio)
			text = text.lower()
			print(text)
	except:
		print("...")
		r = sr.Recognizer()
		continue
