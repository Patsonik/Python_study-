print("Kalkulator, który pierw dodaje twoje liczby, później je mnoży, odejmuje i na końcu dzieli ")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Wynik dodawania", a, " + ", b, "to: ", str(a+b))
print("Wynik mnożenia", a, " * ", b, "to: ", str(a*b))
print("Wynik odejmowania", a, " - ", b, "to: ", str(a-b))
print("Wynik dzielenia", a, " / ", b, "to: ", str(a/b))

print("Czy chciałabyś coś jeszcze zrobić ze swoimi liczbami?")

def wykonaj_dzialanie():
    while True:
        wybor = input("Czy chciałabyś coś zrobić ze swoimi liczbami? (TAK/NIE): ")

        if wybor.upper() == "TAK":
            print("Pierw rozwiąż wybraną macierz metodą Gaussa i wyślij do Pati, to wtedy coś Pati dopisze dalej do kodu i coś zrobię.")
            break
        elif wybor.upper() == "NIE":
            print("Trudno, szkoda, że tak zamulasz łooozaaaaa.")
            break
        else:
            print("Nieprawidłowy wybór.")

        print("Niech matemtyka będzie z TObą!")


wykonaj_dzialanie()
