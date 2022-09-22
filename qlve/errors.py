errors = [
    "Missing Package Name. After the file execution, the Package Name is required.",
    "Missing Command. After the package name, please input the command name."
]

def error(error_code):
    print(errors[error_code])