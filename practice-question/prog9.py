## perform copy command

sfile=input("Enter Source File:")

try:
    sf=open(sfile,"r")

    tfile = input("Enter Target File:")
    tf=open(tfile,"w")

    tf.write(sf.read())

    sf.close()
    tf.close()
    print("File Copied...")
except FileNotFoundError as e:
    print(e)