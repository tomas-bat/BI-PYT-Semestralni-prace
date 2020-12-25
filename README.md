# GUI pro aplikaci ASCII-art generator

Semestrální práce z předmětu BI-PYT. Tomáš Batěk, 2020.

## Shrnutí

Cílem semestrální práce bylo vytvořit grafické uživatelské rozhraní pro CLI aplikaci
[ASCII-art generator](https://github.com/tomas-bat/ASCII-art-generator). Tato aplikace byla vytvořena jako
semestrální práce v předmětu BI-PA2 v LS 2019/20. Jedná se o program napsaný v C/C++, který umí konvertovat obrázky
typu JPEG/PNG do ASCII podoby.

V této semestrální práci se tedy jedná o nadstavbu zmíněné CLI aplikace, která ji bude umět ovládat pomocí GUI.

## Jak spustit program

Před instalací tohoto programu je potřeba mít nainstalovaný Python 3.

1. Stáhnout tento projekt: `git clone https://github.com/tomas-bat/BI-PYT-Semestralni-prace`

2. Nainstalovat potřebné moduly: `pip install -r requirements.txt`

3. Získat spustitelný soubor původní CLI aplikace pomocí připraveného skriptu: `./get_generator.sh`

4. Spustit aplikaci: `python main.py`

Pokud se při nějakém kroku instalace vyskytl problém, vizte prosím sekci 'Problémy při instalaci'

## Ukázka aplikace

## Problémy při instalaci

- Tento program byl vyvíjen pomocí Pythonu 3.8, doporučuji tedy používat tuto verzi Pythonu.
  
- Projekt na Githubu je plánovaný jako veřejný, v tuto chvíli však zatím není.

### Instalace potřebných modulů

Příkaz `pip` by měl být schopen nainstalovat potřebné moduly pro běh této aplikace. Narazil jsem však
na situaci, kdy aplikace odmítala fungovat kvůli problémům s moduly. Tento problém lze vyřešit tak, že
potřebné moduly nainstalujete pomocí příkazu `conda install`, místo `pip install`. K tomu je však
potřeba nainstalovat alespoň [minicondu](https://docs.conda.io/en/latest/miniconda.html).

### Získání spustitelného souboru původní CLI aplikace.

Původní CLI aplikace [ASCII-art generator](https://github.com/tomas-bat/ASCII-art-generator) je vlastní
projekt. Pro funkci této Python aplikace je však potřeba získat spustitelný soubor původní CLI
aplikace, který je výsledkem kompilace projektu.

Pro získání spustitelného souboru původní CLI aplikace je připraven skript, který postupně udělá následující:

1. Stáhne z Githubu projekt původní CLI aplikace do složky '.generator'.

2. Zkompiluje aplikaci pomocí příkazu `make compile`.

3. Přesune spustitelný soubor 'generator' do složky Python projektu a smaže všechny soubory projektu
původní CLI aplikace.
   
Kompilace původní CLI aplikace je navržena pro macOS a Linux. Potřebuje externí knihovny 'libpng' a 'libjpeg'.

