import re
def disemvowel(string):
    # Using regex to subsitute vowels
    return (re.sub("[aeiouAEIOU]","",string))           

# Driver
string = "This website is for losers LOL!"
print(disemvowel(string))