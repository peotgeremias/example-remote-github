import os
from git import Repo
from datetime import datetime

PATH_SSH_KEY = '~/.ssh/id_rsa'
BRANCH = 'main'

git_ssh_identity_file = os.path.expanduser(PATH_SSH_KEY)
git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file

"""
    Define o caminho do repositorio: . 
"""
repo = Repo(".")

"""
    Cria um arquivo com o nome baseado no Timestamp corrente
    e escreve um texto no arquivo criado.
"""
filename = f"./data/{datetime.timestamp(datetime.now())}.txt"
with open(file=filename, mode="w") as f:
    f.write(f"Teste: {datetime.now()}")

"""
    Identifica se ocorreu alguma alteração no repositorio e faz o commit 
    na branch informada.
"""
if repo.is_dirty(untracked_files=True):
    repo.index.add(repo.untracked_files)
    repo.index.commit("This is our first commit")
    with repo.git.custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
        try:
            repo.remotes.origin.push(BRANCH).raise_if_error()
        except Exception as error:
            print(error)