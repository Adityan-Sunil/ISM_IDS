import re
from colorama import Fore, init, Style
def f1(s, log_file):
    x = re.search(r"[\n\s\W]*(\s|\W)*select[\n\s\W]*([a-zA-Z]*|.)[\n\s\W]*from(\s|\W)*", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL,end='')
        return 1

def f2(s, log_file):
    x = re.search(r'(\s|\W)+(OR|OR+|LIKE|RLIKE|CONTACT|VERSION|HOSTNAME|DATADIR|UUID)+(\s|\W)+',s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f3(s, log_file):
    x = re.search(r"(\s|\W)+UNION[^\n]*[\n\s]*SELECT(\s|\W)+", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f4(s, log_file):
    x = re.search(r"(\s|\W)*(\w)*(\s|\W)*=[\n\s\W]*UNION(\s|\W)+", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f5(s, log_file):
    x = re.search(r'(\s|\w)+(ORDER BY|EXTRACTVALUE|ADD CONSTRAINT|ALTER COLUMN|ALTER TABLE|CREATE TABLE|CREATE VIEW|ORDER BY|DROP COLUMN|DROP CONSTRAINT|DROP DATABASE|DROP TABLE|DROP VIEW|DROP INDEX|FOREIGN KEY|FULL OUTER JOIN|INNER JOIN|INSERT INTO SELECT|RIGHT JOIN|SELECT INTO|TRUNCATE TABLE)+(\s)+', s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f6(s, log_file):
    x = re.search(r"(\s|\W)+DELETE(\s|\W)+[a-zA-Z]+", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f7(s, log_file):
    x = re.search(r"(\s|\W)*(SLEEP|COUNT).[0-9]+.#(\s|\W)*", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f8(s, log_file):
    x = re.search(r"(\s|\W)*(AND|OR|NOT|\W)(\s|\W)+[\w]+=[\w]+(\s|\W)*", s, re.IGNORECASE) 
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def f9(s, log_file):
    x = re.search(r"(\s|\W)*(AND|OR|NOT)(\s|\W)+(\w)+(\s|\W)+(WHERE|HAVING|FROM)(\s|\W)*", s, re.IGNORECASE)
    if x is None:
        return 0
    else:
        log_file.write(" ->"+s+"<- ")
        print(Fore.RED, x, Style.RESET_ALL)
        return 1
def verifyString(s, log_file):
    ctr = 0
    ctr += f1(s, log_file)
    ctr += f2(s, log_file)
    ctr += f3(s, log_file)
    ctr += f4(s, log_file)
    ctr += f5(s, log_file)
    ctr += f6(s, log_file)
    ctr += f7(s, log_file)
    ctr += f8(s, log_file)
    ctr += f9(s, log_file)
    if(ctr>=1):
        print(Fore.YELLOW, "Sqli Attempt Detected", Style.RESET_ALL)
        log_file.write(" --SQLI Attempt Detected-- ")
        return True
    return False