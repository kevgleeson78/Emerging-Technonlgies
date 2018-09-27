# no declaration needed for strings int ect
x = "Hello World"
# to print out to console
print(x)

stringTest = "test"

stringTest2 = "test2"

# To concat two strings and store in variable
concatStrings = stringTest + " " + stringTest2

# Print out to screen
print(concatStrings)

# To open a file one is created if none exists.
myHtmlFile = open("/Users/Kevin/Desktop/College Folders/Year 4/Sem 1/Emerging Technologies/Python Examples/testHtml.html", "w")

# A string containing html markup
# Stored in output variable
output = "<html>" \
         "<head>" \
         "<title>Test title</title>"\
         "</head>" \
         "<body>" \
         "<h1>Test Of h1 tag with python</h1>" \
         "</body>"\
         "</html>"

# Write the output variable to the myHtmlFile
myHtmlFile.write(output)

