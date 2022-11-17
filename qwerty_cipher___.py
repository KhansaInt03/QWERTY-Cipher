cov_alp = {
            "a":"1''",  "b":"5''",  "c":"3'",   "d":"3''",  "e":"3'''",
            "f":"4''",  "g":"5''",  "h":"6''",  "i":"8'''", "j":"7''",
            "k":"8''",  "l":"9''",  "m":"7'",   "n":"6'",   "o":"9'''",
            "p":"0'''", "q":"1'''", "r":"4'''", "s":"2''",  "t":"5'''",
            "u":"7'''", "v":"4'",   "w":"2'''", "x":"2'",   "y":"6'''",
            "z":"1'",   "1":"1",    "2":"2",    "3":"3",    "4":"4",
            "5":"5",    "6":"6",    "7":"7",    "8":"8",    "9":"9",
            "0":"0",    " ":" ",   ".":".",  ",":",",  "!":"!",
            "?":"?"
            }

def encrypt_qwertypad():

    text = input("Masukkan text\n>>>").lower()

    # Reading every letter in variable text
    list_alpha = [ i for i in text ]
    print(list_alpha)

    # Calling every key in cov_alpha to check with every letter (i) in list_alpha then added with *
    list_covert = [cov_alp.get(i) + '*' for i in list_alpha]

    print(list_covert)
    print(*list_covert, sep='') # Print without list([]) and separator or spaces from list ([])

def decrypt_qwertypad():

    text_c = input("Masukkan ciphertext\n>>>")

    # Splitting the text by *
    split_ciphertext = text_c.split('*')
    # Getting a list of key and values from dictionary cov_alp
    list_key = list(cov_alp.keys())
    list_value = list(cov_alp.values())

    # Return the key from value (look at index in value then key get called by the value)
    result = [ list_key[list_value.index(i)]  for i in split_ciphertext if i in list_value]

    print(result)

    print(*result, sep='')
