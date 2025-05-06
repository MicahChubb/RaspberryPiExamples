from ecies.utils import generate_key
import binascii
import os, sys, inspect #For dynamic filepaths

def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)

def makeKeys():
  # Create the key pair, store it into variables
  eth_k = generate_key()
  sk_bytes = eth_k.secret  # hex string
  pk_bytes = eth_k.public_key.format(True)  # hex string

  # Encode the byte to a hex value and write out to different files
  with open(execution_path('textfiles/secret.txt'), 'wb') as f:
    f.write(binascii.hexlify(sk_bytes))
  with open(execution_path('textfiles/public.txt'), 'wb') as f:
    f.write(binascii.hexlify(pk_bytes))

  print("generated keys!")

if __name__ == "__main__":
  makeKeys()
