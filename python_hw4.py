Python Homework for 2.6.15
anames = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

#this prints any accession name with a "5" in it
for names in anames: 
    if re.search(r"5", names): 
        print(names)
        
#this prints any accession name with a "e or d"
for names in anames: 
    if re.search(r"(e|d)", names): 
        print(names)

#this prints any accession name that contains the letters d and e in that order
for names in anames: 
    if re.search(r"d.*e", names): 
        print(names)

#this prints any accession name that contains the letters d and e in that order with a single letter between them
for names in anames: 
    if re.search(r"d.e", names): 
        print(names)


#this prints any accession name that contains the letters d and e in any order 
for names in anames: 
    if re.search(r"d.*e", names) or re.search(r"e.*d", names): 
        print(names)
        
#this prints any accession name that start with x or y
for names in anames: 
    if re.search(r"^(x|y)", names): 
        print(names)

#this prints any accession name that starts with x or y and ends in e
for names in anames: 
    if re.search(r"^(x|y).*e$", names): 
        print(names)

#this prints any accession name that contains three or more numbers in a row
for names in anames: 
    if re.search(r"\d\d\d", names): 
        print(names)
        
#or

for names in anames: 
    if re.search(r"\d{3,}", names): 
        print(names)


#this prints any accession names that end with d followed by either a, r or p
for names in anames: 
    if re.search(r"d[arp]", names):
        print(names)
        
#or
for names in anames: 
    if re.search(r"d(a|r|p)", names):
        print(names)

