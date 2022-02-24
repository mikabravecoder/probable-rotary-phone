import os

os.system("wget https://github.com/coder/code-server/releases/download/v4.0.2/code-server-4.0.2-linux-amd64.tar.gz")
os.system("tar xvzf code-server-4.0.2-linux-amd64.tar.gz")
os.system("rm code-server-4.0.2-linux-amd64.tar.gz")
os.system("cd code-server-4.0.2-linux-amd64/bin")
os.system("./code-server --bind-addr 0.0.0.0:8080 --auth none")

