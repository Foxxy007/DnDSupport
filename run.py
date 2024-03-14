import eel
import subprocess, os

HOME = os.path.expanduser('~')
# Start Java backend as a subprocess
try:
    java_process = subprocess.Popen(["java", "-jar", f"{HOME}/Documents/DnD/DnDSupport/java/src/MyProject.jar"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
    os.system("bash build.sh")
# Initialize Eel
eel.init('web')

@eel.expose
def call_java_backend():
    # Read all available output from Java backend
    output_lines = java_process.communicate()
    output = str(b''.join(output_lines).decode().strip())
    return output

print(call_java_backend())

#https://stackoverflow.com/questions/35355225/edit-and-create-html-file-using-python

# with open(f"{HOME}/Documents/DnD/DnDSupport/index.html", "rw") as file:
#     for lines in file
    
# eel.start(f"{HOME}/Documents/DnD/DnDSupport/index.html", size=(400, 300))
