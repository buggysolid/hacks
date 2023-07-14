# mullvad-fastest-country-by-relay.py

Get Mullvad relay with lowest latency.  
    
Use this as a proxy metric to figuring out which country would be the best
one to select to get the lowest latency.  

```
./setup.sh
source runtime/bin/activate
python mullvad-fastest-country-by-relay.py
```

# git-backup.sh

Place in your home directory or wherever you store your git based projects.  

Update the $projects variable with a list of directory names of git projects you already have cloned.  

Run the script and it will stash any local changes you have and pull the latest changes.  

You can view your local changes with git stash list.  
