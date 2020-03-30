import os
from sys import argv

import pikepdf
from pikepdf._qpdf import PasswordError

assert len(argv) == 2, "Usage: python3 crack.py <FILENAME.pdf>"
filename = argv[1]
basename = os.path.splitext(os.path.basename(filename))[0]
output = "cracked_%s.pdf" % basename

# advance month and year
def next_month_year(m,y):
    return 1 + (m%12), y + (m==12)

# bruteforce
m, y = 1, 1
while y < 100:
    m, y = next_month_year(m, y)
    password = "%02d%02d" % (m, y)
    print("Trying %s..." % password, end="")
    try:
        pdf = pikepdf.open(filename, password=password)
        print("SUCCESS")
        print("FOUND PASSWORD: %s" % password)
        pdf.save(output)
        break
    except PasswordError as e:
        print("FAIL")