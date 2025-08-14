#ask user for an md5 hash to crack
hash_input = input("Enter an MD5 hash to crack: ")

#confirm input data
print(f"Hash Received: {hash_input}")

import hashlib

found = False

#open and read a wordlist file
with open("wordlist.txt", "r") as file:
	for line in file:
		test_word = line.strip() # remove newline chars
		hash_word = hashlib.md5(test_word.encode()).hexdigest()

		#compare to users input
		if hash_input == hash_word:
			print(f"Match found! The pass word is {test_word}")
			found = True
			break

if not found:
	print("No match found in wordlist")
