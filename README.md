# Anti-Duplicator

The script takes an input folder, looks through all the files in it
(and all subfolders and sub-folders ...) and reports if it finds
duplicates. Duplicates are two files with the same name and size.

# How to run

Open the terminal, go to the directory where the file is located and
run "**python duplicates.py \[path\]**", if python 3 as not default try
"**python3 duplicates.py \[path\]**". The **path** to the directory is passed as
an **argument** when the file is started

### Example to run

```bash
$ python duplicates.py /home/user/example
File file2.txt has duplicates:
    /home/user/example/file2.txt
    /home/user/example/dir1/file2.txt
File file1.txt has duplicates:
    /home/user/example/file1.txt
    /home/user/example/dir1/file1.txt
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
