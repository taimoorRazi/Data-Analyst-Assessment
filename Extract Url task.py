"""
Assume any database includes below columns and you are requested to process Stats_Access_Link column and extract pure url information inside per device type. 

    Rules: 
-   Xml tags and protocol parts is guaranteed to be lower case  
-   Access link part that we are interested in can have alpha-numeric, case insensitive characters, underscore ( _ ) character and dot ( . ) character only.  

What would you use for this task, please write your detailed answer with exact solution? Please  provide the link to your code as answer to this question 

Example: for the device type AXO145, we would like to get xcd32112.smart_meter.com regardless from its access protocol is SSL secured or not.

"""
# First I created a table in postgres db. And added the values as following

""" 
-- CREATE TABLE url_info_table (
--     Device_Type VARCHAR(50),
--     Stats_Access_Link VARCHAR(500)
-- )
-- INSERT INTO url_info_table (Device_Type, Stats_Access_Link) 
-- VALUES 
-- ('AXO145', '<url>https://xcd32112.smart_meter.com</url>'),
-- ('TRU151', '<url>http://tXh67.dia_meter.com</url>'),
-- ('ZOD231', '<url>http://yT5495.smart_meter.com</url>'),
-- ('YRT326', '<url>https://ret323_TRu.crown.com</url>'),
-- ('LWR245', '<url>https://luwr3243.celcius.com</url>'); """


# Connect to PostgreSQL database
import re
import psycopg2
import pandas as pd
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="goucho10"
)

# Read data from PostgreSQL table into pandas DataFrame
df = pd.read_sql_query("SELECT * FROM url_info_table", conn)

# define a regular expression pattern to extract the URL information
pattern = r'(?:http|https)://([a-zA-Z0-9_\.]+)'

# create a function to extract the URL information for a given device type


def extract_url_info(device_type):
    # filter the dataframe to include only the specified device type
    filtered_df = df[df['device_type'] == device_type]

    # extract the URL information using regular expressions
    urls = []
    for link in filtered_df['stats_access_link']:
        match = re.search(pattern, link)
        if match:
            urls.append(match.group(1))

    # return the list of extracted URLs
    return urls


# test the function for the device type AXO145
urls = extract_url_info('TRU151')
print(urls)
