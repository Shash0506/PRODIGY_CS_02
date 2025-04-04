from PIL import Image
import numpy as np
import os

# Simple key-based pixel modifier
def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    arr = np.array(img)

    # Basic encryption: Add key to each pixel and wrap around using modulo
    encrypted_arr = (arr + key) % 256

    encrypted_img = Image.fromarray(encrypted_arr.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    arr = np.array(img)

    # Reverse operation: Subtract key from each pixel
    decrypted_arr = (arr - key) % 256

    decrypted_img = Image.fromarray(decrypted_arr.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Operation mode")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to output image")
    parser.add_argument("key", type=int, help="Numeric key for encryption/decryption")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input file does not exist.")
        exit(1)

    if args.mode == "encrypt":
        encrypt_image(args.input, args.key, args.output)
    else:
        decrypt_image(args.input, args.key, args.output)
