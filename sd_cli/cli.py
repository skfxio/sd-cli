import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():    
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Welcome to the {bcolors.OKGREEN}SKFX DEV{bcolors.ENDC} cli")
    print()

    name = input(f"Enter project name: {bcolors.OKCYAN}")
    git = input(f"{bcolors.ENDC}GitHub repo origin: {bcolors.OKCYAN}")
    print(f"{bcolors.ENDC}Choose project type")
    print(f"{bcolors.OKBLUE}1{bcolors.ENDC} - aiogram3 bot")
    print(f"{bcolors.OKBLUE}2{bcolors.ENDC} - backend {bcolors.FAIL}(not working yet!){bcolors.ENDC}")
    pr_type = int(input(f"Insert number here:  {bcolors.OKCYAN}")) - 1
    print(bcolors.ENDC)
    
    if pr_type == 1: 
        quit()
    
    templates = [
        {
            "origin": "git@github.com:skfxio/tgbot-template.git",
            "name": "aiogram3 bot",
            "dir": "tgbot-template",
        },
        {
            "origin": "git@github.com:skfxio/sdlib.git",
            "name": "backend",
            "dir": "sdlib",
        },
    ]


    os.system('cls' if os.name == 'nt' else 'clear')

    print("Is everything correct?")
    print()
    print(f"Name:{bcolors.OKGREEN}", name, bcolors.ENDC)
    print(f"Repo:{bcolors.OKGREEN}", git, bcolors.ENDC)
    print(f"Project type:{bcolors.OKGREEN}", templates[pr_type]['name'], bcolors.ENDC)
    print()
    correct = input(f"[{bcolors.OKGREEN}y{bcolors.ENDC}/{bcolors.FAIL}n{bcolors.ENDC}]  ")
    if correct.lower() != "y":
        print(f"{bcolors.FAIL}Quiting...{bcolors.ENDC}")
        quit()

    os.system('cls' if os.name == 'nt' else 'clear')

    os.system(f"git clone {templates[pr_type]['origin']}")
    print(f"{bcolors.OKGREEN}Renaming: {templates[pr_type]['dir']} -> {name}{bcolors.ENDC}")
    os.rename(templates[pr_type]['dir'], name)

    os.chdir(name)

    os.system(f"git remote set-url origin {git}")
    os.system(f"git checkout --orphan temp_branch")
    os.system(f"git add -A")
    os.system(f"git commit -m \"Initial commit by sd-cli with tg-bot-template\"")
    os.system(f"git branch -D master")
    os.system(f"git branch -m master")
    
    
    os.system(f"git push --force origin master")



    os.system(f"python -m venv venv")

    if os.name == "posix":
        os.system("./venv/bin/python -m pip install -r ./requirements.txt")
    if os.name == "nt":
        os.system(".\\venv\\Scripts\\python.exe -m pip install -r .\\requirements.txt")    

    print()
    print()

    print(f"{bcolors.OKGREEN}Finished!{bcolors.ENDC} You can start bot with commands:")
    print(f"cd {name}")

    if os.name == "posix":
        print("source ./venv/bin/activate")
    if os.name == "nt":
        print(".\\venv\\Scripts\\activate")
        
    print(f"python -m bot")

main()