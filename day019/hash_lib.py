#Author:Anliu

import hashlib
m = hashlib.md5()
m.update(b"admin")
print(m.hexdigest())
m.update(b"_123")
print(m.hexdigest())
m1 = hashlib.md5()
m1.update("哈哈admin123".encode())
print(m1.hexdigest())
#print(m1.digest)

hash = hashlib.sha1()
hash.update(b'admin')
print(hash.hexdigest())

hash1 = hashlib.sha256()
hash1.update(b'admin')
print(hash1.hexdigest())

hash2 = hashlib.sha384()
hash2.update(b'admin')
print(hash2.hexdigest())

hash3 = hashlib.sha512()
hash3.update(b'admin')
print(hash3.hexdigest())

import hmac
h = hmac.new(b"admin")
print(h.hexdigest())

