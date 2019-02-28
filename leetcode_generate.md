leetcode_generate Usage Guide
=============================

Preparements:
-------------
Use `selenium`, `requests` and `chromedriver`

Mac Users can install `chromedriver` by `homebrew`

```bash 
$ brew install chromedriver

# Install chromedriver 
$ ln -s /usr/bin/chromedriver /usr/local/bin/chromedriver
```

Install essential packages: `requests`, `selenium`
```bash
$ pip3 install -r requirements.txt
```

Config:
-------

Edit your own username, password, language and repo in the **example.ini** file and then rename it to **config.ini**.
```text
[leetcode]

username = example 
password = example 
language = python3 
repo = https://github.com/example/leetcode
driverpath = /usr/local/bin/chromedriver
```

Run:
----
```bash
# Fully Download (Default you can always run fully download)
$ python3 leetcode_generate.py

# Download by id (You can only download the solution you want. Just add the id arguments behind)
$ python3 leetcode_generate.py 1 100
```

Changelogs:
-----------
- 2019-02-28 Fix the login bug caused by Leetcode change its login page