###########    New Version  PEM    ###########
# Generate a Private Key for the CA
openssl genpkey -algorithm RSA -out cakey.pem -aes256
# Generate a Self-Signed CA Certificate
openssl req -x509 -new -key cakey.pem -out cacrt.pem -days 365
# Generate a Private Key for the User
openssl genpkey -algorithm RSA -out userkey.pem -aes256
# Create a Certificate Signing Request (CSR) for the User
openssl req -new -key userkey.pem -out user.csr
# Sign the User Certificate with the CA Certificate
openssl x509 -req -in user.csr -CA cacrt.pem -CAkey cakey.pem -CAcreateserial -out usercrt.pem -days 365
