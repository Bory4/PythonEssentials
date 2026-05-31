# TryHackMe: Encryption - Crypto 101

![Zakończenie pokoju](Screenshot_20260529_084020.png)

---

### Pytania i odpowiedzi

* **Are SSH keys protected with a passphrase or a password?** passphrase
![Odpowiedź 1](Screenshot_20260529_084109.png)

* **What does SSH stand for?** Secure Shell
* **How do webservers prove their identity?** certificates
* **What is the main set of standards you need to comply with if you store or process payment card details?** PCI-DSS
![Odpowiedź 2](Screenshot_20260529_084122.png)

* **What's 30 % 5?** 0
* **What's 25 % 7?** 4
* **What's 118613842 % 9091?** 3565
![Odpowiedź 3](Screenshot_20260529_084134.png)

* **Should you trust DES? Yea/Nay:** Nay
* **What was the result of the attempt to make DES more secure so that it could be used for longer?** Triple DES
* **Is it ok to share your public key? Yea/Nay:** Yea
![Odpowiedź 4](Screenshot_20260529_084145.png)

* **p = 4391, q = 6659. What is n?** 29239669
![Odpowiedź 5](Screenshot_20260529_084158.png)

* **What can you use to verify that a file has not been modified and is the authentic file as the author intended?** Digital Signature
![Odpowiedź 6](Screenshot_20260529_084213.png)

---

### Polecenia SSH

* Generowanie hasha z klucza prywatnego do formatu obsługiwanego przez John The Ripper:
  `/usr/share/john/ssh2john.py id_rsa_1593558668558.id_rsa`
![Terminal ssh2john](Screenshot_20260529_084307.png)

* Łamanie wygenerowanego hasha przy użyciu słownika rockyou.txt:
  `john --wordlist=/usr/share/wordlists/rockyou.txt --format=SSH ssh.hash`
![Terminal john](Screenshot_20260529_084414.png)

* **What algorithm does the key use?** RSA
* **Crack the password with John The Ripper and rockyou, what's the passphrase for the key?** delicious
![Odpowiedź 7](Screenshot_20260529_084224.png)

---

### Polecenia GPG

* Importowanie klucza:
  `gpg --import tryhackme.key`
![Terminal GPG import](Screenshot_20260529_084445.png)

* Odszyfrowanie pliku wiadomości:
  `gpg --decrypt message.gpg`
![Terminal GPG decrypt](Screenshot_20260529_084503.png)

* **You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?** Pineapple
![Odpowiedź 8](Screenshot_20260529_084530.png)

