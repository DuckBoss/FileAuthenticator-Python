# FileAuthenticator-Python
Compares hashes of any two files (images, text files, binary files, etc) to check identicality.


## Usage Format
This script requires two system arguments consisting of the two files to compare to. 
```
python file_authenticator.py src_file.txt dst_file.txt
```

## Example Run
```
> python file_authenticator.py example_src.txt example_dst.txt
```
```
The Src file and Dst file is IDENTICAL.
MD5 Src File: d39116226466021df4f63dfd80faa59e
MD5 Dst File: d39116226466021df4f63dfd80faa59e
```
