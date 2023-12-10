import os 
import instaloader
import subprocess
import importlib


L = instaloader.Instaloader()
# List of dependencies
dependencies = ["instaloader","subprocess","importlib","os" ]

# Install dependencies
for dependency in dependencies:
    try:
        importlib.import_module(dependency)
    except ImportError:
        print(f"Installing {dependency}...")
        subprocess.run(["pip", "install", dependency])
# Login or load session
L.login("$account", "$password")        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "$profile")

# Print list of followees

follow_list = []
count=0
file = open("houshangi_followers.txt","a+")
for followee in profile.get_followers():
    username = followee.username
    file.write(username + "\n")
    print(username)

file.close()
count=count+1
# (likewise with profile.get_followers())
