import unidecode

def crypt_vigenere_code():
    mes, key = "Jadore écouter la radio toute la journée", "musique"
    encrypted_mess = ""
    clean_mes = str.upper(unidecode.unidecode(mes))
    clean_key = str.upper(unidecode.unidecode(key))
    len_key = len(clean_key)

    for i in range(0, len(clean_mes)):
        char_mes = clean_mes[i]

        if i > len_key - 1:
            return

        if char_mes.isalpha():
            index_mes = ord(char_mes) - ord('A')
            char_key = clean_key[i]
            index_key = ord(char_key) - ord('A')
            index_crypted = (index_mes + index_key)

            if index_crypted > 25:
                index_crypted -= 26

            char_crypted = chr(index_crypted + ord('A'))
            encrypted_mess += char_crypted
            print("encrypted_mess: ", encrypted_mess)
        else:
            encrypted_mess += char_mes

def decrypt_vigenere_code():
    return

if __name__ == '__main__':
    crypt_vigenere_code()