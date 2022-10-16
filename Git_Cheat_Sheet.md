######################################################
# Using WSL
######################################################
There's about 5 operations that you just do over and over. Every once in a while something weird happens and it's tricky to unpack, but nominally it's just doing the same:

    branch -> commit -> PR -> merge -> Repeat

## Using Git
1. open wsl
2. cd to project ex: /mnt/c/Users/MatthewBullis/isubscribed/product-ops/product-ops
3. check status
    git status

## List Branches
To see local branches, run this command:
    git branch
To see remote branches, run this command:
    git branch -r
To see all local and remote branches, run this command:
    git branch -a

# Swtich to a local branch 
    git checkout my-branch-name

# Switch to a Branch That Came From a Remote Repo
To get a list of all branches from the remote, run this command:
    git pull
Run this command to switch to the branch:
    git checkout --track origin/my-branch-name

# Push to a Branch
If your local branch does not exist on the remote, run either of these commands:
    git push -u origin
    git push -u origin HEAD

## branch
To create a new brnach run git checkout -b branch-name
    git checkout -b add-ipynb

## commit
    git add .
    git commit -m "add user-info ipynb"
    git status
    git push -u origin add-ipynb
## PR

## merge
    git status
    git checkout master

git checkout -b add_middleName_and_suffixName
git add . 
git commit -m "add_middleName_and_suffixName"
git push -u origin add_middleName_and_suffixName

git push origin -d commit_offers_campaigns
git branch -D commit_offers_campaigns

Stage Files to Prepare for Commit
1. Enter one of the following commands, depending on what you want to do:

Stage all files: git add .
Stage a file: git add example.html (replace example.html with your file name)
Stage a folder: git add myfolder (replace myfolder with your folder path)
Keep in Mind:

If the file name/path has a space, wrap it in quotes.
You can repeat the above commands for different files and folders.
2. Check the status again by entering the following command:

git status

3. You should see there are changes ready to be committed.

Unstage a File
If you accidental stage something, use the following command to unstage it:

git reset HEAD example.html

Commit Files
1. Enter this command:

git commit -m "Message that describes what this change does"

TIP: For commit messages do you not use past tense, such as "I made headings blue". Use language like "Make headings blue", as if you are giving orders to the codebase. One reason for this is when you work with other people, your code may not be automatically approved. You'll request that they pull your changes into the codebase. When they read the commit messages they will do know what your code will do. Your change will "Make headings blue".

2. Check the status again by running this command:

git status

3. If all changes have been committed, and there are no untracked files, it should say: nothing to commit, working tree clean.


git init
git status
git add "file name.extension"
git status
git branch -M main
git remote add origin-private https://github.com/MatthewBullis/DevUtils.git
git push -u origin-private main



# Import local repo

$ git clone --bare https://external-host.com/EXTUSER/REPO.git
# Makes a bare clone of the external repository in a local directory

$ cd REPO.git
$ git push --mirror https://github.com/USER/REPO.git
# Pushes the mirror to the new repository on GitHub.com


# git clone --bare (Creates bare/empty repo) URL/name for new repo                          local path to repo
# git clone --bare                           https://github.com/MatthewBullis/DevUtils.git "/mnt/c/Users/MatthewBullis/DevUtils"

git clone --bare https://github.com/MatthewBullis/DevUtils.git "/mnt/c/Users/MatthewBullis/DevUtils"

echo "# DevUtils" >> Git_Cheat_Sheet.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MatthewBullis/DevUtils.git
git push -u origin main

mbulliswsl@LAPTOP-E923ANH2:/mnt/c/Users/MatthewBullis/Git_Cheat_Sheet$ git add --all
mbulliswsl@LAPTOP-E923ANH2:/mnt/c/Users/MatthewBullis/Git_Cheat_Sheet$ git commit -m "add util scripts"
mbulliswsl@LAPTOP-E923ANH2:/mnt/c/Users/MatthewBullis/Git_Cheat_Sheet$ git branch -M main
mbulliswsl@LAPTOP-E923ANH2:/mnt/c/Users/MatthewBullis/Git_Cheat_Sheet$ git push -u origin main
mbulliswsl@LAPTOP-E923ANH2:/mnt/c/Users/MatthewBullis/Git_Cheat_Sheet$ 