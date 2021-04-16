# Pyrunner

> Run python code in telegram bot


### How to deploy:

```bash
# Pre Requirement : Python 3

# Install python3 requirements
pip3 install requirements.txt

cp creds_local.conf creds_local.py
# Put credentials in creds_local.py now

# Run the bot
python3 pyrunner.py
```

- Put ids of sudo users in sudo_users.txt. Sudo users will have owner like access

- Put authorized chats ids in authorized_chats.txt