from sys import exit, argv

def xor(data, key):
    key = str(key)
    output_str = ""
    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        o = lambda x: x if isinstance(x, int) else ord(x) # handle data being bytes not string
        output_str += chr(o(current) ^ ord(current_key))
    return output_str

def printCiphertext(ciphertext):
    print(ciphertext)

try:
    #plaintext = open(argv[1], "rb").read()
    plaintext = "fce8820000006089e531c0648b50308b520c8b52148b72280fb74a2631ffac3c617c022c20c1cf0d01c7e2f252578b52108b4a3c8b4c1178e34801d1518b592001d38b4918e33a498b348b01d631ffacc1cf0d01c738e075f6037df83b7d2475e4588b582401d3668b0c4b8b581c01d38b048b01d0894424245b5b61595a51ffe05f5f5a8b12eb8d5d6833320000687773325f54684c772607ffd5b89001000029c454506829806b00ffd5505050504050405068ea0fdfe0ffd5976a0568c0a8e982680200115c89e66a1056576899a57461ffd585c0740cff4e0875ec68f0b5a256ffd568636d640089e357575731f66a125956e2fd66c744243c01018d442410c60044545056565646564e565653566879cc3f86ffd589e04e5646ff306808871d60ffd5bbf0b5a25668a695bd9dffd53c067c0a80fbe07505bb4713726f6a0053ffd5"
except:
    print("File argument needed! %s " % argv[0])
    exit()

def main():
    KEY = "XOt"
    printCiphertext(xor(plaintext, KEY))
if __name__ == '__main__':
    main()