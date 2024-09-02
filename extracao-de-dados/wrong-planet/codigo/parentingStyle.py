import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

request = requests.get('https://wrongplanet.net/forums/viewtopic.php?t=419468')
content = request.content

site = BeautifulSoup(content, 'html.parser')

posts = site.findAll('div', attrs={'class': 'message-col'})


user_names = []
genders = []
messages = []


for post in posts:
    user = post.find_previous_sibling('div', attrs={'class': 'user-col'})
    if user:
        user_name = user.find('a', href=True)
        if user_name:
            user_name = user_name.text.strip()
            user_names.append(user_name)
        
        gender = user.find(string=lambda string: string and 'Gender:' in string)
        if gender:
            gender = gender.split('Gender:')[1].strip()
            genders.append(gender)
        else:
            genders.append(None)
    
    message_content = post.find('div', attrs={'class': 'message-content'})
    if message_content:
        messages.append(message_content.text.strip())
    else:
        messages.append(None)


df = pd.DataFrame({
    'Nome do Usuário': user_names,
    'Gênero': genders,
    'Conteúdo da Mensagem': messages
})

path = "extracao-de-dados\wrong-planet\csv"
fileName = "resultParentStyle.csv"
fullNamePath = os.path.join(path, fileName)

df.to_csv(fullNamePath, index=False)
