import subprocess

# List of script paths
script_paths = [
    r"C:\Artificial_Intelligence\Tokens\Arabic_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Bengali_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\English_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\French_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Hindi(Devanagari)_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Italian_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Japanese(Romaji)_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Korean_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Mandarin(Pinyin)_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Mayan_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Nahuatl_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Polish_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Portuguese_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Punjabi(Gurmukhi)_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Russian_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Spanish_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Tagalog_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Turkish_Token_Creating_Script.py",
    r"C:\Artificial_Intelligence\Tokens\Vietnamese_Token_Creating_Script.py"
]

# Run each script in sequence
for script_path in script_paths:
    try:
        print(f"Running script: {script_path}")
        subprocess.run(["python", script_path], check=True)
        print(f"Successfully ran: {script_path}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}\n")
    except Exception as e:
        print(f"Unexpected error running {script_path}: {e}\n")

print("All scripts have been processed.")