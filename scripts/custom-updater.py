import git
from colorama import Fore, Back, Style



#heavyly based on original code from webUI
def is_outdated(extension,extension_name):
    try:
        repo = git.Repo(extension)
        for fetch in repo.remote().fetch("--dry-run"):
            if fetch.flags != fetch.HEAD_UPTODATE:
                print(Fore.YELLOW + f"===> {extension_name},outdated!🤨")
                return True
            return False
    except Exception as e:
        print(Fore.RED + f'===>Error checking {extension_name}. Please check it manually🙄.<===')
        return False


#heavyly based on original code from webUI
def fetch_and_reset_hard(update_extension,extension_name):
    try:
        repo = git.Repo(update_extension)
        # Fix: `error: Your local changes to the following files would be overwritten by merge`,
        # because WSL2 Docker set 755 file permissions instead of 644, this results to the error.
        repo.git.fetch('--all')
        repo.git.reset('--hard', 'origin')
        print(Fore.GREEN + f"===> {extension_name},updated!😎")
    except Exception as e:
        print(Fore.RED + f'===>Error updating {extension_name}. Please check it manually🙄.<===')
        return False

def ask():
    from inputimeout import inputimeout, TimeoutOccurred  
    try:
        answer = inputimeout(Fore.WHITE + str("\n Update WebUI extensions (y + Enter or Enter (Yes) / Any key (No)): "), timeout=10)
        answer=str(answer).lower()
        if answer=="y" or answer=="":
            return True
        else:
            return False
    except TimeoutOccurred:
        print("\n Cancelling extensions update, WebUI loading continues...\n")
        return False

def update_extensions():
    import os
    counter=1
    extensions_path= os.getcwd().replace("\stable-diffusion-webui-updater\scripts","")
    extensions_path= os.path.join(extensions_path,"extensions")
   
    
    raw_extensions_list= os.listdir(extensions_path)
    cleaned_extension_list=[]
    
    for extension in raw_extensions_list :
        update_extension = os.path.join(extensions_path, extension)
        if os.path.isdir(update_extension):
            cleaned_extension_list.append(update_extension)
            
    for extension in cleaned_extension_list :
        extension_name=update_extension.split("\\")[-1]
        update_extension = os.path.join(extensions_path, extension)
        print(f"Checking {counter} of {len(cleaned_extension_list)-1}:", extension_name, )
        if is_outdated(update_extension,extension_name):
            fetch_and_reset_hard(update_extension,extension_name)
        counter+=1



if __name__ == "__main__": 
    if ask():
        update_extensions()
    else:
        quit()
