#!/usr/bin/env python3
"""Encrypt an HTML file with AES-256-GCM for client-side decryption."""
import os, json, base64, hashlib, sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def encrypt_html(input_path, password):
    with open(input_path, 'r') as f:
        plaintext = f.read()
    
    salt = os.urandom(16)
    iv = os.urandom(12)
    
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600000)
    key = kdf.derive(password.encode('utf-8'))
    
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext.encode('utf-8'), None)
    
    return {
        'salt': base64.b64encode(salt).decode(),
        'iv': base64.b64encode(iv).decode(),
        'ct': base64.b64encode(ciphertext).decode()
    }

password = sys.argv[1]

# Encrypt dashboard
data = encrypt_html('/home/gideo/clawd/projects/keenai-site/dashboard-raw.html', password)
print(json.dumps(data))
