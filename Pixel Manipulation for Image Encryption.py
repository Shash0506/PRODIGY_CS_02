from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    img_array = np.array(image)
    
    # Apply XOR encryption using the key
    encrypted_array = img_array ^ key
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    img_array = np.array(image)
    
    # Apply XOR decryption (same as encryption)
    decrypted_array = img_array ^ key
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    action = input("Enter 'encrypt' or 'decrypt': ").strip().lower()
    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    key = int(input("Enter an encryption key (0-255): "))
    
    if action == "encrypt":
        encrypt_image(input_path, output_path, key)
    elif action == "decrypt":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")
