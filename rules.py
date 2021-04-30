import re

def f2(s):
    x = re.search(r'(\s+)(OR|OR+|LIKE|CONTACT|VERSION|HOSTNAME|DATADIR|UUID)+(\s+)',s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        print(x)
        return 1
def f3(s):
    x = re.search(r"(\s+)UNION[^\n]*[\n\s]*SELECT(\s+)", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        print(x)
        return 1
def f4(s):
    x = re.search(r"[?][\n\s]*=[\n\s]*UNION(\s+)", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        print(x)
        return 1
def f5(s):
    x = re.search(r'(\s+)(ADD CONSTRAINT|ALTER COLUMN|ALTER TABLE|CREATE TABLE|CREATE VIEW|DROP COLUMN|DROP CONSTRAINT|DROP DATABASE|DROP TABLE|DROP VIEW|DROP INDEX|FOREIGN KEY|FULL OUTER JOIN|INNER JOIN|INSERT INTO SELECT|RIGHT JOIN|SELECT INTO|TRUNCATE TABLE)+(\s+)', s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        print(x)
        return 1
def f6(s):
    x = re.search(r"(\s+)DELETE(\s+)[a-zA-Z]+", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        print(x)
        return 1

def verifyString(s):
    ctr = 0
    ctr += f2(s)
    ctr += f3(s)
    ctr += f4(s)
    ctr += f5(s)
    ctr += f6(s)
    if(ctr>=1):
        print("sqli detected")
        return True
    return False