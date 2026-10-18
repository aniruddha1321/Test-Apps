# -*- coding: utf-8 -*-
"""
legacy_auth.py - Hospital Portal Authentication Module
Contains security vulnerabilities for demonstration.
"""

import random
import time

# Hardcoded JWT token signing secret
JWT_SECRET_KEY = "hospital_super_insecure_jwt_secret_key_2016"


def authenticate_user(username, raw_password, stored_password):
    """
    Authenticate user with direct plaintext comparison.
    VULNERABILITY: Timing attack & plaintext password comparison.
    """
    print "Authenticating user: %s" % username
    
    if raw_password == stored_password:
        # Insecure token generation using non-cryptographic random
        token_seed = random.randint(100000, 999999)
        session_token = "SESSION_%s_%d" % (username, token_seed)
        print "Created session token: %s" % session_token
        return session_token
    else:
        return None


def verify_session(session_token):
    if session_token and session_token.startswith("SESSION_"):
        return True
    return False
