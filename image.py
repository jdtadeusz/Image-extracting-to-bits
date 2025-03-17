import cv2
import os
import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import others

def imageImport(url, fileName):
    if not os.path.exists(fileName) :
        r = requests.get(url + fileName, allow_redirects=True)
        open(fileName, 'wb').write(r.content)


    print("Importing the image...")

    others.clearConsole()
    
    I = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
    print("\nImage successfully read.")
    time.sleep(0.5)

    plt.imshow(I, cmap='gray')
    plt.title('Obraz w skali szarości')
    plt.show()

def imageExtracting(I):
    img = cv2.imread(I, cv2.IMREAD_GRAYSCALE)

    if I is None:
        print("Nie można wczytać obrazu.")
        return
    
    start_time = time.time()

    bit_images = []

    print("\nPrzetwarzanie obrazu...")

    for bit in range(8):
        bit_plane = ((img >> bit) & 1) * 255
        bit_images.append(bit_plane.astype(np.uint8))
    
    end_time = time.time()

    print(f"\nPrzetwarzanie zakonczone sukcesem!\nCzas przetwarzania: {end_time - start_time:.2f} sekund\nWcisnij enter aby wyswitlic przetworzone obrazy...")
    input()

    return bit_images

def displayBits(bit_images):
    output_folder = 'extracted_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for bit, bit_plane in enumerate(bit_images):
        cv2.imshow(f"Bit {bit}", bit_plane)
        output_path = os.path.join(output_folder, f"bit_{bit}.png")
        cv2.imwrite(output_path, bit_plane)
        print(f"Extracted images saved in: {output_path}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def reconstructImage(bit_images, num_bits, output_folder = "reconstructed_images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    reconstructed_image = np.zeros_like(bit_images[0], dtype=np.uint16)

    for i in range(num_bits):
        reconstructed_image += bit_images[7 - i] * (2**(0 + i))

    reconstructed_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)

    output_path = os.path.join(output_folder, f"reconstructed_{num_bits}_bits.jpg")
    cv2.imwrite(output_path, reconstructed_image)
    print(f"Obraz zrekonstruowany z {num_bits} bitow zapisany w: {output_path}")