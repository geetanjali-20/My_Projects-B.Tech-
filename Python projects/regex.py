import re
string="Hi Everyone ,Hey this is Geetanjali Sharma"
pattern="Hi"

m=re.match(pattern,string).group(0)

print(m)
string="Hi Everyone,Hey this is Geetanjali Sharma"
pattern="Hey"

m=re.search(pattern,string).group(0)

print(m)
import re
string="India is a democratic country and Delhi is the capital of India."
pattern="India"

m = re.findall(pattern,string)
n = re.finditer(pattern,string)
print(m)
for i in n:
    print(i.start())
