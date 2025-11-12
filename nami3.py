import hashlib

def crack_md5_hash(hash, wordlist):
    with open(wordlist, 'r', encoding='latin-1') as f:
        for line in f:
            word = line.strip()
            md5_hash = hashlib.md5(word.encode()).hexdigest()
            if md5_hash == hash:
                return word
    return None

# Example usage
hash_to_crack = 'bd6992f34897caffba03ebb8dcdd731e'
wordlist_file = '/usr/share/wordlists/rockyou.txt'

password = crack_md5_hash(hash_to_crack, wordlist_file)
if password:
    print(f"Password found: {password}")
else:
    print("Password not found in wordlist")
