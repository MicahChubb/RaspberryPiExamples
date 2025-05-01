# Asymmetric Encryption
We will be using Asymmetric Encryption to "securely" transfer the information for our transaction. Something to keep in mind is that this is for demonstration purposes only.

The way this type of encryption works is that we generate 2 keys, one that is public that we use to encrypt and one that is private to decrypt. The message can *only* be decrypted by the private key, this is what makes it secure. You can get more information about this idea in [this video](https://www.youtube.com/watch?v=GSIDS_lvRv4).

In our example, we will generate some keys, and then encrypt and then decrypt a message. For your assignment, you should modify this to encrypt your card number, CVC and money amount, then decrypt on the "bank" end.
![Bank of Bear diagram](https://github.com/MicahChubb/RaspberryPiExamples/blob/main/asymmetricEncryption/bank.drawio.png?raw=true)

You will need:

```pip install eciespy``` 

You can use all the scripts separately or use the main.py which has a simple command line interface to control what you do. I would recommend reading each script and thinking about how it works.

## Further information:
* https://pypi.org/project/eciespy/
* https://blog.finxter.com/how-to-write-a-hex-string-as-binary-data-binary-file-in-python/
