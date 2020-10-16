import hashlib
import bcrypt

if __name__ == '__main__':
    pswrd_input = input('Please Enter A Password: ')                        # Get Password from User
    hashed = bcrypt.hashpw(pswrd_input.encode(), bcrypt.gensalt())          # Use Bcrypt to Hash Password
    print('Hash of ', pswrd_input, ' is ', hashed.hex())                    # Display Hashed Password in Hexadecimal
