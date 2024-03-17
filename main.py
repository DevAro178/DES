from key import Key
from dataypes import DataTypes
from message import Message

if __name__ == "__main__":
    dt=DataTypes()
    mg=Message()
    k_ins = Key()
    
    # Step 1 - Key Generation
    User_Key=input("Enter a 64-bit Key (01234567): ") or '01234567'
    subkeys=k_ins.generate(User_Key)
    
    # Step 2 - Message Encryption/Decryption
    # Encryption Module
    file = open('plainText.txt', 'r')
    plain_text = file.read()
    file.close()
    cipher_text=mg.encrypt(subkeys,plain_text)
    file = open('cipherText.txt', 'w')
    file.write(cipher_text)
    file.close()
    print('Encryption Done')
    
    # Decryption Module
    cipher_file = open('cipherText.txt', 'r')
    cipher_text = cipher_file.read()
    cipher_file.close()
    plain_text=mg.decrypt(subkeys,cipher_text)
    file = open('cipherDecrypted.txt', 'w')
    file.write(plain_text)
    file.close()
    print('Decryption Done')