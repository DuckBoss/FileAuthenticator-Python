import hashlib
import sys

if len(sys.argv) != 3:
    print("ERROR: This script requires 3 total system arguments.")
    print("FORMAT: python file_authenticator.py <src_file> <dst_file>")
    sys.exit(1)

src_file = sys.argv[1]
dst_file = sys.argv[2]
BUFFER_SIZE = 65536  # 64kb chunks

md5_src = hashlib.md5()
with open(src_file, 'rb') as src:
    while True:
        data_src = src.read(BUFFER_SIZE)
        if not data_src:
            break
        md5_src.update(data_src)

md5_dst = hashlib.md5()
with open(dst_file, 'rb') as dst:
    while True:
        data_dst = dst.read(BUFFER_SIZE)
        if not data_dst:
            break
        md5_dst.update(data_dst)

src_digest = md5_src.hexdigest()
dst_digest = md5_dst.hexdigest()

if src_digest == dst_digest:
    print("The Src file and Dst file is IDENTICAL.")

else:
    print("The Src file and Dst file is DIFFERENT.")

print("MD5 Src File: %s" % src_digest)
print("MD5 Dst File: %s" % dst_digest)
