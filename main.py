import sympy

"""
Requirement:
    [1] Request user 2 input Prime Numbers.
    [2] Request user to input message to encrypt.
    [3] Generte public key and print
    [4] Generate private key and print
    [5] Encrypt message
    [6] Decrypt message and print decrypted message
    [7] Ensure Encrypted message same as Decrypted message 
"""

def generate_key(p:int, q:int):
    """
    
    """
    N = p*q
    pie_N = (p-1)*(q-1)

    # lock encryption
    cofactors_of_N = []
    coprime_of_N = []
    coprime_of_pie_N = []
    for numbers in range(1, N+1): # take common factor of N
        if N % numbers != 0 and N:    
            cofactors_of_N.append(numbers)

    for numbers in cofactors_of_N: # take common prime factor of N
        if numbers % 2 != 0:
            coprime_of_N.append(numbers)

    for count in coprime_of_N: # take common prime factor between N and pie_N
        if count > 1 and count <pie_N:
            if pie_N % count != 0:
                coprime_of_pie_N.append(count)

    e = coprime_of_pie_N[0] # store as e value
    public_key = (e,N)

    multiple_of_e = []
    # for count in range(pie_N+1, pie_N*2):
    for count in range(1, pie_N):
        multiple_of_e.append(e*count)

    possible_keys = []
    for i,v in enumerate(multiple_of_e):
        if v % pie_N == 1:
            possible_keys.append(i+1)

    d = possible_keys[0]
    private_key = (d, N)

    print("Public Key = ",public_key)
    print("Private_Key = ",private_key)
    return public_key, private_key

def isPrime(n):
    return sympy.isprime(n)

def encryption(public_key, text):
    e,n = public_key
    p = pow(text , e, n)
    return p

def decryption(private_key, text):
    d,n = private_key
    p = pow(text , d, n)
    return p

def format_message(input_string):
    list_ascii = []
    for i in range(len(input_string)):
        list_ascii.append(ord(input_string[i]))
    return list_ascii

def encrypt_string(public_key, input_string):
    list_ascii_p = format_message(input_string)
    # print("list_ascii_numbers(BEFORE ENCRYPTION) : ", list_ascii_p)
    list_cipher_ascii = []
    for i in list_ascii_p:
        list_cipher_ascii.append(encryption(public_key, i))
    # print("list_ascii_numbers(AFTER ENCRYPTION) : ", list_cipher_ascii)
    return list_cipher_ascii

def decrypt_string(private_key, list_cipher_ascii):
    list_decrypted_ascii = []
    for i in list_cipher_ascii:
        list_decrypted_ascii.append(decryption(private_key, i))
    return list_decrypted_ascii

def convert_ascii_to_char(list_items):
    char_list = ""
    for i in range(len(list_items)):
        char_list += (chr(list_items[i] % 0x10ffff))
    return char_list

def main():
    """
    Steps:
        [1] user input integer prime number 1 & 2
        [2] user input plan text to encrypt
        [3] generate key based on prime number entered by user
        [4] public key used to encrypt, private key used to decrypt
        [5] Ensure decrypted message same as plain message
    """
    print('\n###############-------------Output-------------###############')
    prime_number_1 = int(input("Enter prime number 1: "))
    if not isPrime(prime_number_1):
        raise ValueError(f"{prime_number_1} is not prime")
    prime_number_2 = int(input("Enter prime number 2: "))
    if not isPrime(prime_number_2):
        raise ValueError(f"{prime_number_2} is not prime")
    message = input('Please enter message to encrypt: ')

    encryption_key = generate_key(prime_number_1, prime_number_2) # ((x,y),(a,b))
    public_key = encryption_key[0] # (x,y)
    private_key = encryption_key[1] # (a,b)

    encrypted_text = encrypt_string(public_key, message) 
    decrypted_text_ascii = decrypt_string(private_key, encrypted_text)
    decrypted_text = convert_ascii_to_char(decrypted_text_ascii)

    print(f'Decrypted Message = {decrypted_text}')

    if decrypted_text == message:
        print("Decryption succesfull!")
    else:
        print("looks like there is a problem with decryption.")

    
if __name__ == '__main__':
    main()

