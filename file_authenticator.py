import sys
import auth_api

if len(sys.argv) != 3:
    print("ERROR: This script requires 3 total system arguments.")
    print("FORMAT: python <this_script.py> <src_file> <dst_file>")
    sys.exit(1)

src_file = sys.argv[1]
dst_file = sys.argv[2]
BUFFER_SIZE = 65536  # 64kb chunks


src_digest = auth_api.file_auth(src_file, BUFFER_SIZE)
dst_digest = auth_api.file_auth(dst_file, BUFFER_SIZE)

if src_digest == dst_digest:
    print("The Src file and Dst file is IDENTICAL.")

else:
    print("The Src file and Dst file is DIFFERENT.")

print("MD5 Src File: %s" % src_digest)
print("MD5 Dst File: %s" % dst_digest)
