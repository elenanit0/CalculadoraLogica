'''
Schreibe ein Programm, das Temperaturen in verschiedene 
Skalensystemen ineinander umwandelt. 
Das Programm soll zu Beginn eine Auswahl mit den verschiedenen Möglichkeiten anbieten:

(1) Umrechnung von Celsius nach Kelvin
(2) Umrechnung von Celsius nach Fahrenheit
(3) Umrechnung von Kelvin nach Celsius
(4) Umrechnung von Kelvin nach Fahrenheit
(5) Umrechnung von Fahrenheit nach Celsius
(6) Umrechnung von Fahrenheit nach Kelvin

Bemerkung:
Celsius = 5/9 * (Fahrenheit - 32).
Celsius = Kelvin - 273.15.
Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K.

Hinweise:
Benuzte if - elif - else
'''

# Eingaben
auswahl = int(input("Gebe mal deine Auswahl ein:\n" +
                "(1) Umrechnung von Celsius nach Kelvin\n" +
                "(2) Umrechnung von Celsius nach Fahrenheit\n" +
                "(3) Umrechnung von Kelvin nach Celsius\n" +
                "(4) Umrechnung von Kelvin nach Fahrenheit\n" +
                "(5) Umrechnung von Fahrenheit nach Celsius\n" +
                "(6) Umrechnung von Fahrenheit nach Kelvin\n"))

original_T = float(input("Gebe mal eine Temperatur ein: "))
# NUEVO COMENTARIO
# bo
# Berechnung und ausgabe:
#(1) Umrechnung von Celsius nach Kelvin
if auswahl == 1:
    if original_T >= -273.15:
        print(original_T + 273.15, "K")
    else:
        print("Die tiefste mögliche Temperatur ist -273.15°C!")

# (2) Umrechnung von Celsius nach Fahrenheit
elif auswahl == 2:
    if original_T >= -273.15:
        print(original_T * 1.8 + 32, "F")
    else:
        print("Die tiefste mögliche Temperatur ist -273.15°C!")

# (3) Umrechnung von Kelvin nach Celsius
elif auswahl == 3:
    if original_T >= 0:
        print(original_T - 273.15, "°C")
    else:
        print("Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K!")

# (4) Umrechnung von Kelvin nach Fahrenheit
elif auswahl == 4:
    if original_T >= 0:
        print(original_T * 1.8 - 459.67, "F")
    else:
        print("Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K!")

# (5) Umrechnung von Fahrenheit nach Celsius
elif auswahl == 5:
    if original_T >= -459.67:
        print((original_T - 32) / 1.8, "°C")
    else:
        print("Die tiefste mögliche Temperatur ist -459.67F!")

# (6) Umrechnung von Fahrenheit nach Kelvin
elif auswahl == 6:
    if original_T >= -459.67:
        print((original_T + 459.67) / 1.8, "K")
    else:
        print("Die tiefste mögliche Temperatur ist -459.67F!")
else:
    print("Sorry, ich habe dich nicht verstanden.")