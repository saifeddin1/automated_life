import git
import os

def simple_git():
	print("*"*50)
	print("*"*20+"By: SAIFEDDIN"+"*"*17+"\n")

	r = git.Repo.init()
	basepath = os.getcwd()
	dirs = os.listdir(basepath)
	dirs.remove('.git')
	

	r.index.add(dirs)

	r.index.commit("Initial commit")

	remote = r.create_remote('origin', url=input("Paste the url of the remote : "))	

	print("Remote added successfuly")
	print("Don't forget to run 'git push origin master' !")
	print('Finallizing ...done !')


simple_git()