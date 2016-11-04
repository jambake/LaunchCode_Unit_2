import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    return ''.join(random.choice(string.leters) for x in xrange(5))

#print make_salt()

# implement the function make_pw_hash(name, pw) that returns a hashed password
# of the format:
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return "%s, %s" % (h, salt)

# Implement the function valid_pw() that returns True if a user's password
# matches its hash. You will need to modify make_pw_hash.

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)
#h = make_pw_hash('spez', 'hunter2')
#print valid_pw('spez', 'hunter2', h)
