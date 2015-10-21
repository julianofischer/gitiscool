from apiwrapper import ApiWrapper

def get_local_repo_info():
    username = None
    reponame = None

    try:
        with open(".git/config",'r') as f:
            for line in f:
                if 'url' in  line:
                    line = line.split(":")
                    line = line[1].split("/")
                    username = line[0]
                    reponame = line[1]
                    reponame = reponame[:-5] #removing ".git"
                    break


    except Exception as e:
        print("Exception while reading repository information.")
        print(e.message)

    return (username,reponame)

def main():
    username, reponame = get_local_repo_info()
    print (username)
    print (reponame)
    wrapper = RepoWrapper()
    wrapper.get_repo(username, reponame)

if __name__ == "__main__":
    main()
