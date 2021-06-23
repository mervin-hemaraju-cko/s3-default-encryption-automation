# S3 Bucket Encryption

This script will enable the default encryption for S3 buckets on a list of bucket names provided in a file.

The script will also generate results file so that you will know if all buckets has been successfully modified.

The script makes use of the underlying AWS CLI.

There are 3 scripts provided in the repo:

* enforce_enc.py

* backout_enc.py

* fetch_enc.py


### enforce_enc.py

This script is used to enforce the default encryption on the given list of buckets.

To run the command, type ```python enforce_enc.py```


### backout_enc.py

In case you need to rollback, this script will remove the encryption enforced on the given list of buckets.

To run the command, type ```python backout_enc.py```


### fetch_enc.py

This script is used to verify the encryption enforce on the given list of buckets.

To run the command, type ```python fetch_enc.py```