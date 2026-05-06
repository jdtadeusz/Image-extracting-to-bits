# Image Extracting to Bits

Projekt do ekstrakcji i rekonstrukcji obrazów na poziomie bitów. Program pozwala na wyodrębnienie poszczególnych płaszczyzn bitowych z obrazu oraz rekonstrukcję obrazu z wybranej liczby bitów.

## Opis

Ten projekt implementuje zaawansowaną analiz�� obrazów poprzez:
- **Ekstrakcję bitów**: Rozbija obraz na 8 płaszczyzn bitowych (bit 0-7)
- **Wizualizację**: Wyświetla każdą płaszczyznę bitową jako osobny obraz
- **Rekonstrukcję**: Odtwarza oryginalny obraz używając wybranej liczby bitów

Projekt jest idealny do nauki przetwarzania obrazów, zrozumienia reprezentacji binarnej pikseli oraz eksploracji wpływu poszczególnych bitów na jakość obrazu.

## Wymagania

```
Python 3.x
opencv-python (cv2)
numpy
matplotlib
requests
```

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/jdtadeusz/Image-extracting-to-bits.git
cd Image-extracting-to-bits
```

2. Zainstaluj wymagane pakiety:
```bash
pip install opencv-python numpy matplotlib requests
```

## Użycie

Uruchom program:
```bash
python main.py
```

### Przebieg programu:

1. **Import obrazu** - Program automatycznie pobiera przykładowy obraz (100zloty.jpg) z internetu i wyświetla go
2. **Ekstrakcja bitów** - Obraz jest przetwarzany i dzielony na 8 płaszczyzn bitowych
3. **Wizualizacja** - Wyodrębione płaszczyzny bitowe są wyświetlane i zapisywane w folderze `extracted_images/`
4. **Rekonstrukcja** - Program pyta, czy chcesz zrekonstruować obraz z wybranej liczby bitów (1-8)

```
Czy chcialbys zrekonstruowac obraz z danej ilosci bitow?
1. Tak
2. Nie
```

Wpisz liczbę od 1 do 8, aby wybrać, ile bitów (od najstarszego bitu) chcesz wykorzystać do rekonstrukcji.

## Struktura projektu

- **main.py** - Główny plik programu, obsługa interfejsu użytkownika
- **image.py** - Funkcje do przetwarzania obrazów:
  - `imageImport()` - Import i wyświetlenie obrazu
  - `imageExtracting()` - Ekstrakcja płaszczyzn bitowych
  - `displayBits()` - Wyświetlenie i zapis wyodrębnionych bitów
  - `reconstructImage()` - Rekonstrukcja obrazu z wybranej liczby bitów
- **others.py** - Funkcje pomocnicze (czyszczenie konsoli)

## Dane wyjściowe

Program tworzy dwa foldery z plikami:
- **extracted_images/** - Zawiera 8 plików `bit_0.png` do `bit_7.png` (poszczególne płaszczyzny bitowe)
- **reconstructed_images/** - Zawiera zrekonstruowane obrazy `reconstructed_X_bits.jpg`

## Przykład

Dla obrazu 100 PLN program wyodrębnia poszczególne bity:
- **Bit 7-4** (najstarsze bity) - Zawierają główne cechy obrazu, jego ogólny kształt
- **Bit 3-0** (najmłodsze bity) - Zawierają szczegóły i szumy obrazu

Rekonstrukcja z 4 bitów da wyraźny, uproszczony obraz, a z 8 bitów - pełną jakość oryginału.

## Technologia

- **OpenCV** - Przetwarzanie obrazów
- **NumPy** - Operacje numeryczne i bitowe
- **Matplotlib** - Wizualizacja
- **Requests** - Pobieranie obrazów z internetu

## Autor

jdtadeusz

## Licencja

Brak określonej licencji. Projekt jest dostępny publicznie na GitHub.

---

**Ostatnia aktualizacja**: 2026-05-06
