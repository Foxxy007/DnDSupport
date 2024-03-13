import eel
import subprocess

# Start Java backend as a subprocess
java_process = subprocess.Popen(["java", "-jar", "/Users/theman/Documents/DnD/DnDPythonSupport/MyProject.jar"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

# with open("/Users/theman/Documents/DnD/DnDPythonSupport/index.html", "rw") as file:
#     for lines in file
    
# eel.start('/Users/theman/Documents/DnD/DnDPythonSupport/index.html', size=(400, 300))
