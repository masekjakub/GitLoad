#pip install gitpython
import os
import git

projectsFolder = '/home/gary/Projects/'

repoUrl = input("Repo url:")
repoName = repoUrl.split("/")[-1]
repoDir = os.path.join(projectsFolder,repoName)

print(repoDir)
try:
    repo = git.Repo.init(repoDir)
    repo.clone_from(repoUrl,repoDir)
except:
    print("Repository is already existing!")
