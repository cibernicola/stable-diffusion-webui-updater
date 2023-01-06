import git
import os



#heavyly based on original code from webUI
def is_outdated(extension,extension_name):
    try:
        path=os.path.join(extension, ".git")
        repo = git.Repo(path)
        for fetch in repo.remote().fetch("--dry-run"): 
            if fetch.flags != fetch.HEAD_UPTODATE:
                print(f"===> {extension_name},outdated!")
                status['outdated']+=1
                return True
            return False
    except Exception as e:
        status['error_checking']+=1
        status['error_updating']+=1
        status['unknown_status']+=1
   
        print(f"===> Error checking {extension_name} <===\
            \n    Unable to read repository info from {path}. \
            \n    Please check it manually.\
            \n-----------------------------------------")
        
        print("\n")

        return False


#heavyly based on original code from webUI
def fetch_and_reset_hard(update_extension,extension_name):
    try:
        repo = git.Repo(update_extension)
        # Fix: `error: Your local changes to the following files would be overwritten by merge`,
        # because WSL2 Docker set 755 fasdgsdgjdgfhkfghjlghjñk´hkjile permissions instead of 644, this results to the error.
        repo.git.fetch('--all')
        repo.git.reset('--hard', 'origin')
        print(f"===> {extension_name},updated!")
        status['updated']+=1
    except Exception as e:
        print(f'===>Error updating {extension_name}. Please check it manually.<===\n', str(e))
        status['error_updating']+=1
        return False

def ask():
    from inputimeout import inputimeout, TimeoutOccurred  
    try:
        answer = str(inputimeout(str("\n Update WebUI extensions. (y + Enter or Enter (Yes) / Any other key + Enter (No)): "), timeout=10)).lower()
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
    status["total_extensions"] = len(cleaned_extension_list)
    
    for extension in cleaned_extension_list :
        extension_name=extension.split("\\")[-1]
        update_extension = os.path.join(extensions_path, extension)
        print(f"Checking {counter} of {status['total_extensions']}:", extension_name, )
        if is_outdated(update_extension,extension_name):
            fetch_and_reset_hard(update_extension,extension_name)
        counter+=1
    


if __name__ == "__main__": 
    
    global status
    status={
    "updated":0,
    "outdated":0,
    "error_checking":0,
    "error_updating":0,
    "total_extensions":0,
    "unknown_status":0
    }
    if ask():
        update_extensions()
        print(f"\n-==Update status==- \n -Extensions:{status['total_extensions']} \
                                    \n -Outdated:{status['outdated']} \
                                    \n -Updated:{status['updated']} \
                                    \n -Errors checking:{status['error_checking']} \
                                    \n -Errors updating:{status['error_updating']} \
                                    \n -Unknown status:{status['unknown_status']} \
                                    \n --------- \n ")
    else:
         print("\n Cancelling extensions update, WebUI loading continues...\n")