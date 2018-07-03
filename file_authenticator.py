import hashlib
import sys

if len(sys.argv) != 3:
    print("ERROR: This script requires 3 total system arguments.")
    print("FORMAT: python <this_script.py> <src_file> <dst_file>")
    sys.exit(1)

src_file = sys.argv[1]
dst_file = sys.argv[2]
BUFFER_SIZE = 65536  # 64kb chunks


def file_auth(file_name):
    md5 = hashlib.md5()
    with open(file_name, 'rb') as src:
        while True:
            data_src = src.read(BUFFER_SIZE)
            if not data_src:
                break
            md5.update(data_src)
    return md5.hexdigest()


src_digest = file_auth(src_file)
dst_digest = file_auth(dst_file)

if src_digest == dst_digest:
    print("The Src file and Dst file is IDENTICAL.")

else:
    print("The Src file and Dst file is DIFFERENT.")

print("MD5 Src File: %s" % src_digest)
print("MD5 Dst File: %s" % dst_digest)
