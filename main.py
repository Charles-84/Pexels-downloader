from pypexels import PyPexels
import json
import requests


# Initialisez la bibliothèque PyPexels avec votre clé API
api_key = "API_KEY"
api_client = PyPexels(api_key)

print(api_client.api_version)
for i in range(100) :
    # Recherchez des vidéos correspondant à la recherche
    videos = api_client.videos_search(query='WHAT_YOU_ARE_LOOKING_FOR', per_page=80, page=i)
    # Convertir l'objet 'videos' en dictionnaire Python
    videos_dict = videos._body

    # Extraire les liens de téléchargement de chaque vidéo
    # Écrire les liens de vidéos trouvés dans un fichier texte
    with open('pexels.txt', 'a+') as file:
        for link in videos_dict['videos']:
            file.write(link['url'] + '\n')

videos = []

# Extraire l'ID et le titre de chaque vidéo
with open('pexels.txt', 'r') as file:
    for line in file:
        # Extraire l'ID de la vidéo à partir de l'URL
        video_id = line.strip().split('/')[-2]
        video_id = ''.join(filter(str.isdigit, video_id))
        # Extraire le titre de la vidéo à partir de l'URL
        video_title = line.strip().split('/')[-2].split('-' + video_id)[0].replace('-', ' ').title()

        videos.append({'id': video_id, 'title': video_title})

with open('pexels.json', 'w') as file:
    json.dump(videos, file, indent=4)


# Télécharger les vidéos
with open('pexels.json', 'r') as file:
    videos = json.load(file)
    num_downloaded_videos = 0
    max_num_videos = 80000
    for video in videos:
        if num_downloaded_videos >= max_num_videos:
            break

        # Construire l'URL de téléchargement de la vidéo à partir de son ID
        video_url = f'https://www.pexels.com/video/{video["id"]}/download/'

        # Envoyer une requête GET à l'URL de téléchargement pour récupérer le contenu de la vidéo
        response = requests.get(video_url)

        # Si la requête a réussi, enregistrer le contenu de la vidéo dans un fichier
        if response.status_code == 200:
            video_data = response.content
            filename = f'{video["title"]} ({video["id"]}).mp4'
            with open(f"Vidéo/{filename}", 'wb') as file:
                file.write(video_data)
            num_downloaded_videos += 1
            print(f'Téléchargement de la vidéo {num_downloaded_videos}: {filename}')
        else:
            print(f'Erreur lors du téléchargement de la vidéo {video["id"]}')

print(f'Téléchargement de {num_downloaded_videos} vidéos terminé !')
