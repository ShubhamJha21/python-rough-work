import re
my_str = "+919876544567+919876544567,+919876544567 +919876544567 19876544567 +919876544567+929876544567,+929876544567,+929876544567,+929876544567,+929876544567,+929876544567,+929876544567"
patt = re.compile(r"\+91\d{10}")
matches= patt.findall(my_str)
list = []
for match in matches:
    list.append(match)
print("list of all mo no is\n",list)
