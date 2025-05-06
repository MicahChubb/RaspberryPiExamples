from ecies import encrypt
import binascii
import os, sys, inspect #For dynamic filepaths

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)
    
def encryptMessage(data):
    # Read in from our text file, convert from hex to a byte
    with open(execution_path('textfiles/public.txt')) as f:
        for line in f:
            pk_hex = binascii.unhexlify(''.join(line.split()))

    # Encrypt the test string and then write out to a file as hex
    encryptedMessage = encrypt(pk_hex, data.encode("utf8"))
    with open(execution_path('textfiles/encrypted.txt'), 'wb') as f:
        f.write(binascii.hexlify(encryptedMessage))
    
    print("encrypted message!")

if __name__ == "__main__":
  encryptMessage('this is some test data')
