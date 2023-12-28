#Daniel Almond project 4
import os
import json

# Directory of the account files. Will be used to write the encrypted files at the end
directory = "" # put your file directory here

# Function to find the files to be analyzed. Searches the directory for text files.
def get_file_paths(dir):
    # When a text file is found, add it to the list of files.
    encr_files = []
    with os.scandir(dir) as folders:
        for folder in folders:
            if not folder.is_file():
                with os.scandir(dir + "/" + folder.name) as files:
                    for file in files:
                        if file.name.endswith(".txt"):
                            encr_files.append(file)        
    return encr_files

# Function to find the keywords needed to decrypt. Not needed anymore...
def get_keywords(dir):
    keywords = []
    with os.scandir(dir) as filepaths:
        for filepath in filepaths:
            if filepath.name == "keywords.txt":
                with open(filepath, "r") as file:
                    text = file.read().strip()
                    keywords = text.split()
    return keywords

# Function to get the text data from the file.
def load_data(encrypted_file):
    print("Loading data...")
    try:
        # Read each file and return its contents
        with open(encrypted_file, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("You don't have permission to read this file!")

# Function to decrypt text data from the file.
def decrypt(encrypted_file):
    print("Decrypting...")
    # Brute force and try all ascii values to decrypt.
    for key in range(128):
        decrypted_file = ''.join(chr((ord(char) - key) % 128) for char in encrypted_file)
        # If the data has recognizable key words, accept the file data.
        if "Password" in decrypted_file or "Username" in decrypted_file and len(decrypted_file) > 0:
            return decrypted_file

# Function to parse the file
def parse_file(content):
    print("Parsing file...")
    try:
        # Parse the data into readable dictionaries.
        parsed_data = json.loads(content)
        return parsed_data
    except TypeError:
        return "Cannot parse this file!"

# Function to check if account data is correct
def data_validation(accounts_data):
    print("Validating data...")
    missing_data = 0
    # If the account is a list, check for each key. If an account has a key missing,
    # increase missing_data by 1
    if type(accounts_data) != str:
        for account in accounts_data:
            try:
                account['Username']

            except KeyError:
                missing_data += 1
                continue
            try:
                account['Password']
               
            except KeyError:
                missing_data += 1
                continue
            try:
                account['Email']
               
            except KeyError:
                missing_data += 1
                continue
            try:
                account['Date Created']
            except KeyError:
                missing_data += 1
                continue
            try:
                account['Last Login']
            except KeyError:
                missing_data += 1
                continue
            try:
                account['Account Balance']
            except KeyError:
                missing_data += 1
                continue
            try:
                account['Account Number']
            except KeyError:
                missing_data += 1
                continue
    return missing_data


# Function to check password strength.
def password_check(accounts):
    print("Checking for weak passwords...")
    weak_passwords = 0
    # If the account is a list, check the account keys for a password
    if type(accounts) != str:
        for account in accounts:
            try:
                password = account['Password']
            except KeyError:
                continue
            #  Judge each password by following criteria:
            # needs an uppercase letter
            has_upper = False
            # needs a lowercase letter
            has_lower = False
            # needs a digit
            has_digit = False
            # needs a special character
            has_special_char = False
            # needs to be 8 characters or more
            has_length_8 = False

            # check each password for criteria
            if len(password) >= 8:
                has_length_8 = True
            for char in password:
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
                try:
                    if int(char) == type(int):
                        has_digit = True
                except ValueError:
                    pass
                if ord(char) <= 100:
                    has_special_char = True

            # if password does not meet all requirements, increase amount of weak passwords by 1
            if not (has_upper and has_lower and has_digit and has_special_char and has_length_8):
                weak_passwords += 1
   
    return weak_passwords

# Function to check for duplicate accounts.
def duplicate_account(accounts):
    print("Checking for duplicate accounts...")
    potential_duplicates = 0
    # If the account is a list, check the accounts for duplicate emails and account numbers
    if type(accounts) != str:
        # iterate through list of accounts
        for i in range(len(accounts)):
            duplicate = False
            # compare the account at index i to all other accounts that come after
            j = i + 1
            while j < len(accounts):
                try:    
                    if accounts[i]['Email'] == accounts[j]['Email']:
                        duplicate = True              
                except KeyError:
                    pass

                try:
                    if accounts[i]['Account Number'] == accounts[j]['Account Number']:
                        duplicate = True 
                except KeyError:
                    pass
               
                # if any accounts have the same email or account number, increase count of duplicate accounts by 1
                if duplicate:
                    potential_duplicates += 1

                j += 1

    return potential_duplicates

# Function to reencrypt the file.
def reencrypt(decrypted_file, directory, file):
    print("Reencrypting data...")
    # Create new key. Default is 12
    key = 12
    # Encrypt old file data with new key
    encrypted_data = ''.join(chr((ord(char) + key) % 128) for char in decrypted_file)
   
    # Create new file and write the encrypted data on it.
    # Each file is prefixed with 'reencrypted_'
    # The files will be written in the original directory from the beginning
    with open(directory + "reencrypted_" + file.name, 'w') as file:
        file.write(encrypted_data)
        print("Encrypted data written at " + file.name)

# Write the final report
def final_report(total_accounts, total_files, total_weak_passwords, total_duplicate_accounts, num_empty_files):
    # Calculate percentages
    percent_empty_files = (num_empty_files / total_files) * 100
    percent_total_missing_data = (total_missing_data / total_accounts) * 100
   
    print("FINAL REPORT:")
    print("=====================================")
    print(f"Reviewed {total_files} files.")
    print(f"Could not read {num_empty_files} files.")
    print(f"Total accounts analyzed: {total_accounts}")
    print(f"Total accounts with missing data: {total_missing_data}")
    print(f"% of accounts with missing data: {percent_total_missing_data}%")
    print(f"% of files that could not be decrypted: {percent_empty_files}%")
    print(f"Total accounts with weak passwords: {total_weak_passwords}")
    print(f"Total potential duplicate accounts: {total_duplicate_accounts}")
    print("-------------------------------------")
    print("Major challenges encountered were account dictionaries with missing keys and some keys in the account dictionaries being misspelled.")
    print("Recommendations are to make sure all relevant data is in the account dictionary and to make sure dictionary keys are spelled correctly.")

# List for the empty files encountered
empty_files = []
# Count for accounts with missing data
total_missing_data = 0
# Count for all accounts reviewed
total_accounts = 0
# Count for all weak passwords encountered
total_weak_passwords = 0
# Count for all duplicate accounts encountered
total_duplicate_accounts = 0

# Fetch all files from the directory
data = get_file_paths(directory)
# Fetch keywords from the key word file. Not used anymore...
keylist = get_keywords(directory)

# Look through each file
for file in data:
    current_file = load_data(file)
    # If file is empty, add it to the empty file list
    # Print response and go to the next file
    if len(current_file) == 0:
        empty_files.append(file)
        print(f"Could not read {file.name}...")
        print("=====================================")
        continue
    print(f"Opening {file.name}...")
    # Decrypt file data
    decrypted_data = decrypt(current_file)
    # Parse file for list of accounts
    accounts = parse_file(decrypted_data)
   
    # Amount of accounts in the file
    file_accounts = len(accounts)
    # Amount of accounts with missing data in the file
    file_missing_data = data_validation(accounts)
    # Amount of weak passwords in file
    file_weak_passwords = password_check(accounts)
    # Amount of duplicate accounts in file
    file_duplicate_accounts = duplicate_account(accounts)
    # % of accounts with missing data in file
    file_missing_data_percent = file_missing_data / file_accounts
   
    # add # of accounts, missing data, weak passwords, and duplicate accounts to the total
    total_accounts += file_accounts
    total_missing_data += file_missing_data
    total_weak_passwords += file_weak_passwords
    total_duplicate_accounts += file_duplicate_accounts
   
    # Reencrypt file data
    reencrypt(current_file, directory, file)

    # Print out report for stats within the file
    print("-------------------------------------")
    print(f"Accounts in this file: {file_accounts}")
    print(f"Missing data in file: {file_missing_data}")
    print(f"Percent of missing data in file: {file_missing_data_percent * 100}%")
    print(f"Weak passwords in this file: {file_weak_passwords}")
    print(f"Potential duplicate accounts: {file_duplicate_accounts}")
    print("=====================================")

# Count total files
total_files = len(data)
# Count total empty files
num_empty_files = len(empty_files)

# Create final report based on data collected
final_report(total_accounts, total_files, total_weak_passwords, total_duplicate_accounts, num_empty_files)