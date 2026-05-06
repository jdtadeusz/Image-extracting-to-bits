# Image Extracting to Bits

Projekt do ekstrakcji i rekonstrukcji obrazów na poziomie bitów. Program pozwala na wyodrębnienie poszczególnych płaszczyzn bitowych z obrazu oraz rekonstrukcję obrazu z wybranej liczby bitów.

## Opis

Ten projekt implementuje zaawansowaną analizę obrazów poprzez:
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

## Technologia

- **OpenCV** - Przetwarzanie obrazów
- **NumPy** - Operacje numeryczne i bitowe
- **Matplotlib** - Wizualizacja
- **Requests** - Pobieranie obrazów z internetu
