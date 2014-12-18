# Write a program that can parse a large web server access log file with a regular syntax 
# and outputs the top N most frequently occurring URLs (not IP addresses) in descending order.
import re

def parseWebLog(log, N=0):
    cache = {}
    result = []
    urls = match(log)
    for url in urls:
        if url not in cache:
            cache[url] = 1
        else:
            cache[url] += 1
    for url in cache:
        result.append([url, cache[url]])
    result = sorted(result, key=lambda url: url[1], reverse=True)
    if N >= len(result) or N == 0:
        return result
    else:
        return result[:N]

# Match looks for urls in the log file and returns a list of all the urls in the file
def match(log):
    urls = []
    # If we're handling a file that requires more memory than available, use the file object as an iterator.
    # Using `with` ensures that each line is read and then garbage collected after it has been read,
    # so we aren't storing the entire read file in memory. It also closes the file once iteration is complete.
    with open(log) as f:
        for line in f:
            info = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
            urls.append(info[7])
    return urls

# Follow up question:
# What if the log file is an order of magnitude larger than the available disk space?
# How would you store it and parse it?

# If the log file is larger than the available disk space, one possibility is to utilize 
# a buffer to view a manageable slice of the file at a time. For each buffer, we'd have to
# keep track of the position of that particular buffer slice in relation to the actual file.
# We'd then handle each slice the same way, while keeping one ubiquitous record of all the 
# urls that show up in each buffer. 
