from sys import argv
import errors
import json

input_info = False

try:
    package = argv[1]
except:
    errors.error(0)
    quit()
    
try:
    command = argv[2]
except:
    errors.error(1)
    quit()

if command == "*":
    input_info = True

if input_info == False:
    with open(f"packages/{package}/package/{command}.py") as f:
        for i in f.readlines():
            exec(i)
elif input_info == True:
    with open(f"packages/{package}/.json") as f:
        info = json.load(f)
        print(f"""
Name: {info["name"]}
Version: {info["version"]}
        """)