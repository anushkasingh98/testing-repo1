from github import Github

g = Github("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") # Expiring on 20th June 2023
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# trying to get repo : https://github.com/anushkasingh98/Habit-Tracker

# for repo in g.get_user().get_repos():
#     print(repo.name)

repo = g.get_repo("anushkasingh98/Habit-Tracker")
print(repo.downloads_url)
# print(repo.get_contents(repo.downloads_url))

import os
cwd = os.getcwd()
path = cwd+"/test"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")

contents = repo.get_contents("")
ignore_files = [".DS_Store","LICENSE","README.md"]
i=0
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        if(file_content.name not in ignore_files):
            new_path = path+"/"+file_content.name
            isExist = os.path.exists(path+"/"+file_content.name)
            if isExist:
                new_path = path+"/duplicate"+str(i)+"/"+file_content.name
                isExist = os.path.exists(path+"/duplicate"+str(i))
                if not isExist:
                    os.makedirs(path+"/duplicate"+str(i))
                i+=1
            f = open(new_path, "wb")
            print(file_content.name)
            print(type(file_content.decoded_content))
            f.write(file_content.decoded_content)
            # print(type(file_content.content))
            f.close()
