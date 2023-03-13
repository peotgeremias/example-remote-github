import os
from git import Repo
from git import Git
from datetime import datetime

PATH_SSH_KEY = '~/.ssh/id_rsa'
BRANCH = 'main'
REPOSITORY = 'git@github.com:peotgeremias/example-repo.git'

git_ssh_identity_file = os.path.expanduser(PATH_SSH_KEY)
git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file


# with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
#     repo = Repo.clone_from(REPOSITORY, 'example-repo', branch=BRANCH)



r = Repo(".")

filename = f"{datetime.timestamp(datetime.now())}.txt"
with open(file=filename, mode="w") as f:
    f.write(f"Teste: {datetime.now()}")


# with r.git.custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
# 	r.remotes.origin.fetch()
 
if r.is_dirty(untracked_files=True):
    r.index.add(r.untracked_files)
    r.index.commit("This is our first commit")
    with r.git.custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
        try:
            r.remotes.origin.push(BRANCH).raise_if_error()
        except Exception as error:
            print(error)