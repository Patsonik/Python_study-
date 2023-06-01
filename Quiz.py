# @todo Implement me
def getFileContent(fileName):
    return "Function should read the file content and return it"

# @todo Implement me
def printQuestion(fileName):
    fileContent = getFileContent(fileName)
    print("The proper question should be displayed based on the file content")

# @todo Implement me
def getUserAnswer():
    return "Return the answer typed by the user"

# @todo Implement me
def getPoints(fileName, answer):
    fileContent = getFileContent(fileName)
    return 1 # Based on the file and the user's answer, this function should provide the received points

def quiz2():
    punkty = 0
    
    # Pytanie 1
    printQuestion("question1.txt")
    answer = getUserAnswer()
    punkty += getPoints("answer1.txt", answer)
    
    # Pytanie 2
    printQuestion("question2.txt")
    answer = getUserAnswer()
    punkty += getPoints("answer2.txt", answer)
    
    # Pytanie 3
    printQuestion("question3.txt")
    answer = getUserAnswer()
    punkty += getPoints("answer3.txt", answer)
    
    # Pytanie 4
    printQuestion("question4.txt")
    answer = getUserAnswer()
    punkty += getPoints("answer4.txt", answer)
    
    # Pytanie 5
    printQuestion("question5.txt")
    answer = getUserAnswer()
    punkty += getPoints("answer5.txt", answer)
    
    # Wynik
    print("\nMożna było zdobyć od 0 do 10 punktów, a ty masz", punkty, "punktów.")
    print("Ave Pati!")



def quiz():
    punkty = 0
    
    # Pytanie 1
    print("Pytanie 1: Czy lubisz matmę?")
    print("A. Tak i to bardzo !!!")
    print("B. Nie lubię, to jest głupie")
    print("C. Najbardziej na świecie to ja lubię Pati")
    odpowiedz1 = input("Odpowiedź: ")
    
    if odpowiedz1 == "A":
        punkty += 1
    elif odpowiedz1 == "C":
        punkty += 2
    
    # Pytanie 2
    print("\nPytanie 2: Jakie lody lubisz najbardziej?")
    print("A. Czekoladowe")
    print("B. Waniliowe")
    print("C. Owocowe")
    odpowiedz2 = input("Odpowiedź: ")
    
    if odpowiedz2 == "A":
        punkty += 2
    elif odpowiedz2 == "C":
        punkty += 2
    
    # Pytanie 3
    print("\nPytanie 3: Czy lubisz sport?")
    print("A. Tak uwielbiam Sport!")
    print("B. Nie lubię, to jest głupie")
    print("C. Najbardziej to ja lubię Pati")
    odpowiedz3 = input("Odpowiedź: ")
    
    if odpowiedz3 == "A":
        punkty += 1
    elif odpowiedz3 == "C":
        punkty += 2
    
    # Pytanie 4
    print("\nPytanie 4: Jakie miałaś/eś myśli kiedy mnie pierwszy raz zobaczyłaś/eś?")
    print("A. Woooow ale laska, piękna inteligenta i elokwentna!")
    print("B. Wooow chciałabym z nią chodzić!")
    print("C. Odpowiedzi A i B są prawidłowe")
    odpowiedz4 = input("Odpowiedź: ")
    
    if odpowiedz4 == "A" or odpowiedz4 == "B":
        punkty += 1
    elif odpowiedz4 == "C":
        punkty += 2
    
    # Pytanie 5
    print("\nPytanie 5: Czy chciałabyś/łbyś rozwiązywać zagadki chodząc po górach?")
    print("A. Oczywiście to jeden z najlepszych sposób na spędzenie wolnego czasu!!!")
    print("B. Nie, bo to głupie")
    print("C. Wszystko z Pati jest cudowne")
    odpowiedz5 = input("Odpowiedź: ")
    
    if odpowiedz5 == "A":
        punkty += 1
    elif odpowiedz5 == "C":
        punkty += 2
    
    # Wynik
    print("\nMożna było zdobyć od 0 do 10 punktów, a ty masz", punkty, "punktów.")
    print("Ave Pati!")

quiz()
