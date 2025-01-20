import gnupg

# Initialize the GPG object
gpg = gnupg.GPG()

# Path to the ASCII-armored private key file
private_key_file = 'privatekey.asc'

# Read the private key
with open(private_key_file, 'r') as f:
    private_key_data = f.read()

# Import the private key
import_result = gpg.import_keys(private_key_data)

# Check the import result to ensure the key was imported successfully
if import_result.count == 0:
    raise ValueError('Failed to import the private key.')

# Get the fingerprint of the imported key
fingerprint = import_result.fingerprints[0]

# Unlock the private key using the passphrase
passphrase = 'Test123!@#'

# Path to the file to be signed
file_to_sign = 'TestConnection.py'

# Sign the file
with open(file_to_sign, 'rb') as f:
    signed_data = gpg.sign_file(f, keyid=fingerprint, passphrase=passphrase)

# Check if the signing was successful
if signed_data:
    signed_file_path = 'TestConnection.asc'
    with open(signed_file_path, 'wb') as sf:
        sf.write(signed_data.data)
    print(f"File signed successfully and saved to {signed_file_path}.")
else:
    print("Failed to sign the file.")
