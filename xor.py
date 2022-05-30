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
    print('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')

try:
    plaintext = open(argv[1], "rb").read()
    #plaintext = "Hello World!"
except:
    print("File argument needed! %s " % argv[0])
    exit()

def main():
    KEY = "x"
    printCiphertext(xor(plaintext, KEY))
if __name__ == '__main__':
    main()