"""
Write a Python function to convert unix timestamp to human readable format.

unix_timestamp = 1609931401
"""


from datetime import datetime
def convert_timestamp(unix_timestamp):
    return (datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
