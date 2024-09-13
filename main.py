import unidecode

key_string = "musique"
decrypted_message = "J'adore écouter la radio toute la journée"
encrypted_message = "V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY"

def encrypt_vigenere_code():
    mess, key = decrypted_message, key_string
    encrypted_mess = ""
    clean_mess = str.upper(unidecode.unidecode(mess))
    clean_key = str.upper(unidecode.unidecode(key))
    len_key = len(clean_key)
    key_index = 0

    for i in range(len(clean_mess)):
        char_mess = clean_mess[i]

        if char_mess.isalpha():
            char_key = clean_key[key_index % len_key]
            key_index += 1

            index_mess = ord(char_mess) - ord('A')
            index_key = ord(char_key) - ord('A')
            index_crypted = (index_mess + index_key)

            if index_crypted > 25:
                index_crypted -= 26

            char_crypted = chr(index_crypted + ord('A'))
            encrypted_mess += char_crypted
        else:
            encrypted_mess += char_mess

    return encrypted_mess

def decrypt_vigenere_code():
    crypted_mess, key = encrypted_message, key_string
    clean_crypted_mess = str.upper(unidecode.unidecode(crypted_mess))
    clean_key = str.upper(unidecode.unidecode(key))
    len_key = len(clean_key)
    decrypted_mess = ""

    key_index = 0

    for index in range(len(clean_crypted_mess)):
        char_crypted_mess = crypted_mess[index]

        if char_crypted_mess.isalpha():
            char_key = clean_key[key_index % len_key]
            key_index += 1

            index_crypted_mess = ord(char_crypted_mess) - ord('A')
            index_key = ord(char_key) - ord('A')
            index_decrypted = (index_crypted_mess - index_key)

            if index_decrypted < 0:
                index_decrypted += 26

            char_decrypted = chr(index_decrypted + ord('A'))
            decrypted_mess += char_decrypted
        else:
            decrypted_mess += char_crypted_mess

    print("decrypted_mess: ", decrypted_mess)

    return decrypted_mess

if __name__ == '__main__':
    encrypt_vigenere_code()
    decrypt_vigenere_code()