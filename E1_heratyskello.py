from datetime import datetime
import time
import winsound

heratysaika = input("Syötä herätysaika 'HH:MM:SS'")

tunti = int(heratysaika[0:2])
minuutti = int(heratysaika[3:5])
sekunti = int(heratysaika[6:8])

aika = datetime.now()
heratys = datetime(aika.year, aika.month, aika.day, tunti, minuutti, sekunti)

odotus_sekunnit = (heratys-aika).total_seconds()

time.sleep(odotus_sekunnit)
print("Herätys!")
winsound.Beep(410,300)
#winsound.PlaySound()
