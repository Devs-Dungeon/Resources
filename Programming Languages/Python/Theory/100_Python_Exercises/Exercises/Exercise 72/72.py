#Create a script that let the user type in a search term and opens and search on the browser for that term on Google

import webbrowser

query = input("Enter your Google query: ")
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)
webbrowser.open_new(url)
