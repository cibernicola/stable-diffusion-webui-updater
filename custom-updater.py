import git

def is_outdated(extension):
    repo = git.Repo(extension)
    for fetch in repo.remote().fetch("--dry-run"):
        if fetch.flags != fetch.HEAD_UPTODATE:
            print("==>",extension.split("\\")[-1],"outdated")
            return True
        return False


def fetch_and_reset_hard(update_extension):
    repo = git.Repo(update_extension)
    # Fix: `error: Your local changes to the following files would be overwritten by merge`,
    # because WSL2 Docker set 755 file permissions instead of 644, this results to the error.
    repo.git.fetch('--all')
    repo.git.reset('--hard', 'origin')
    print("===>",update_extension.split("\\")[-1], "updated!")

def ask():
    from inputimeout import inputimeout, TimeoutOccurred   
    try:
        answer = inputimeout(prompt=str("\n Update WebUI extensions (Y/any key(No)): "), timeout=10)
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
    extensions_path= os.getcwd().replace("\stable-diffusion-webui-updater","")
    extensions_path= os.path.join(extensions_path,"extensions")
    #extensions_path="L:\stable-diffusion-webui\extensions"
    extensions_list= os.listdir(extensions_path)
    extension_list=[]
    
    for extension in extensions_list :
        update_extension = os.path.join(extensions_path, extension)
        if os.path.isdir(update_extension):
            extension_list.append(update_extension)
            
    for extension in extension_list :
        update_extension = os.path.join(extensions_path, extension)
        print(f"Checking {counter} of {len(extensions_list)-1}:", update_extension.split("\\")[-1], )
        if is_outdated(update_extension):
            fetch_and_reset_hard(update_extension)
        counter+=1
        
if __name__ == "__main__": 
    if ask():
        update_extensions()
    else:
        quit()
