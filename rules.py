import re

def f2(s):
    x = re.search(r'[OR%20|OR|OR+|%0A|OR/*|LIKE|CONTACT|VERSION|HOSTNAME|DATADIR|UUID]',s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        return 1
def f3(s):
    x = re.search(r"UNION[^\n]*[\n\s]*SELECT", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        return 1
def f4(s):
    x = re.search(r"[?][\n\s]*=[\n\s]*UNION", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        return 1
def f5(s):
    x = re.search(r'ADD CONSTRAINT|ALTER COLUMN|ALTER TABLE|CREATE TABLE|CREATE VIEW|DELETE [.]+|DROP COLUMN|DROP CONSTRAINT|DROP DATABASE|DROP TABLE|DROP VIEW|DROP INDEX|FOREIGN KEY|FULL OUTER JOIN|INNER JOIN|INSERT INTO SELECT|RIGHT JIN|SELECT INTO|TRUNCATE TABLE', s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        return 1

def verifyString(s):   
    ctr=0
        
    ctr += f2(s)
    ctr += f3(s)
    ctr += f4(s)
    ctr += f5(s)

    if(ctr>=1):
        print(ctr)
        return True
    return False