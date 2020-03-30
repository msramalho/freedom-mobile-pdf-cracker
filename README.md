# Freedom Mobile Canada | Payment Information PDF Cracker
Freedom Mobile is a SIM card company in Canada.

After creating an account with [freedommobile.ca](freedommobile.ca), an email will be sent with the following instructions:

```
To open the file, you will need to enter a password. 
The password is your date of birth in MMYY format, where MM is the two digits of your
month of birth and YY is the last two digits of your year of birth. For example, 
if you were born on October 9, 1978 then your password would be 1078.
```

This is a ridiculous attempt at security that can be broken with simple bruteforce.

To run the python script, you need to install [pikepdf](https://github.com/pikepdf/pikepdf). You can do so with either of the following options (feel free to use virtual environments):
* `pip install pikepdf`
* `pip install -r requirements.txt`

To do so call `python3 crack.py <FILENAME>`.

After that, just wait a few seconds (you can watch the console) and a new file `cracked_FILENAME.pdf` will be generated.
