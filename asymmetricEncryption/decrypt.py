from ecies import decrypt
import binascii
import os, sys, inspect #For dynamic filepaths

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)	

def decryptMessage():
  # Read in and un-hex our private key
  with open(execution_path('textfiles/secret.txt')) as f:
    for line in f:
      sk_bytes = binascii.unhexlify(''.join(line.split()))

  # Read in and un-hex our message
  with open(execution_path('textfiles/encrypted.txt')) as f:
    for line in f:
      data = binascii.unhexlify(''.join(line.split()))

  # Decrypt our message and write it out!
  decryptedMessage = decrypt(sk_bytes, data)
  print("Decrypted:", decryptedMessage.decode("utf8")) #The decode is to remove a b'text here' formatting

if __name__ == "__main__":
  decryptMessage()
