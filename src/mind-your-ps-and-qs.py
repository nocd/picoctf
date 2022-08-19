# mind-your-ps-and-qs

CHALLENGE = "MIND YOUR PS AND QS"
DESCRIPTION = "In RSA, a small e value can be problematic, but what about N? Can you decrypt this?"
REFERENCES = [
        "https://www.cs.drexel.edu/~jpopyack/Courses/CSP/Fa17/notes/10.1_Cryptography/RSA_Express_EncryptDecrypt_v2.html",
        "https://www.dcode.fr/rsa-cipher",
        "https://www.geeksforgeeks.org/security-of-rsa/",
        "https://www.johndcook.com/blog/2018/12/12/rsa-exponent/"    
]
FLAG = "picoCTF{sma11_N_n0_g0od_73918962}"
SOLUTION = "Go to https://www.dcode.fr/rsa-cipher and enter the values for C, N and E then click Calculate/Decrypt."

def print_challenge():
    print(CHALLENGE)
    print("")

def print_description():
    print("**** DESCRIPTION ****")
    print(DESCRIPTION)
    print("")

def print_references():
    print("**** REFERENCES ****")
    for r in REFERENCES:
        print(r)
    print("")
        
def print_flag():
    print("**** FLAG ****")
    print(FLAG)
    print("")


def print_solution():
    print("**** SOLUTION ****")
    print(SOLUTION)
    print("")


if __name__ == "__main__":
    print_challenge()
    print_description()
    print_references()
    print_flag()
    print_solution()
