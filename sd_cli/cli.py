import os
import subprocess

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the SKFX DEV cli")
    print()

    name = input("Enter project name: ")
    git = input("GitHub repo origin: ")
    print()
    print("Choose project type")
    print("1 - aiogram3 bot")
    print("2 - backend")
    pr_type = int(input("Insert number here: ")) - 1

    templates = [
        {
            "origin": "git@github.com:skfxio/tgbot-template.git",
            "name": "aiogram3 bot"
        },
        {
            "origin": "git@github.com:skfxio/sdlib.git",
            "name": "backend"
        },
    ]


    os.system('cls' if os.name == 'nt' else 'clear')

    print("Is everything correct?")
    print()
    print("Name:", name)
    print("Repo:", git)
    print("Project type:", templates[pr_type]['name'])
    print()
    correct = input("[y/n]  ")
    if correct.lower() != "y":
        print("Quiting...")
        quit()

    os.system('cls' if os.name == 'nt' else 'clear')

    os.system(f"git clone {templates[pr_type]['origin']}")
    print("Renaming: tgbot-template ->", name)
    os.rename("tgbot-template", name)

    os.chdir(name)

    os.system(f"git remote set-url origin {git}")
    os.system(f"git checkout --orphan temp_branch")
    os.system(f"git add -A")
    os.system(f"git commit -m \"Initial commit by sd-cli with tg-bot-template\"")
    os.system(f"git branch -D master")
    os.system(f"git branch -m master")
    
    # print(subprocess.getstatusoutput("git push --force origin master"))
    
    os.system(f"git push --force origin master")



    os.system(f"python -m venv venv")

    if os.name == "posix":
        os.system("./venv/bin/python -m pip install -r ./requirements.txt")
    if os.name == "nt":
        os.system(".\\venv\\Scripts\\python.exe -m pip install -r .\\requirements.txt")    

    print()
    print()

    print("Finished! You can start bot with commands:")
    print(f"cd {name}")

    if os.name == "posix":
        print("source ./venv/bin/activate")
    if os.name == "nt":
        os.system(".\\venv\\Scripts\\activate")
        
    print("python -m bot")


# main()
