import asyncio
import random

class Osoba(ime,id):
    self.ime = ime
    self.id = random

odgovor = input("Želite li zaprimiti obrazac? Da(d)/Ne(n)")

#citanje imena iz filea
if odgovor=="d":
    with open('imena.txt') as f:
        imena = f.readlines()
        print(imena)




#funkcije za sleep
    async def random_sleep(counter: float) -> None:
        delay = random.random() * 5
        print(f"{counter} sleeps for {delay:.2f} seconds")
        await asyncio.sleep(delay)
        print(f"{counter} awakens, refreshed")


    async def sleepers(how_many: int = 5) -> None:
        print(f"Creating {how_many} tasks")
        tasks = [asyncio.create_task(random_sleep(i)) for i in range(how_many)]
        print(f"Waiting for {how_many} tasks")
        await asyncio.gather(*tasks)


else:
        print("Žao nam je. Morati će te upotrijebiti drugi program.")

#if __name__ == "__main__":
    #asyncio.run(sleepers(5))
    #print("Done with the sleepers")

"""
Napraviti Python kod koji će:
na ulazu primiti zahtjev za obradu

Svaki zahtjev otvara novi process, kreira PID (Process ID)

Zahtjev za obradu čita listu imena (potrebno samostalno generirati liste)
za svako ime će kreirati po jedan objekt nakon određenog kašnjenja (kasnjenje je slučajno)

Kašnjenje je atribut objekta

Objekt nakon kreiranja šalje ispis o svom procesu i imenu

Sustav treba moći zaprimati nove zahtjeve dok obrađuje kašnjenja

Napraviti simulator ulaza

Zahtjevi za pokretanjem istog koda stizu svakih delta ms

Vrijeme međudolazaka zahtjeva je ulazni parameter
"""