from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return get_random_bytes(16)

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = pad(data.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_data(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

def main():
    # Key generation (should be done securely and stored properly)
    key = generate_key()

    # Data pegawai yang akan dienkripsi
    data_pegawai = "Nama: FIRMAN !@#$%^&*, Gaji: Rp.5.000.000, Jabatan: $#@!@$#$"

    # Enkripsi data pegawai
    encrypted_data = encrypt_data(data_pegawai, key)
    print(f"Data Pegawai (Sebelum Enkripsi): {data_pegawai}")
    print(f"Data Pegawai (Setelah Enkripsi): {encrypted_data}")

    # Dekripsi data pegawai
    decrypted_data = decrypt_data(encrypted_data, key)
    print(f"Data Pegawai (Setelah Dekripsi): {decrypted_data}")

if __name__ == "__main__":
    main()
