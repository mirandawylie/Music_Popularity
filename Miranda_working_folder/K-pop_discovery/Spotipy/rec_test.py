import requests

url = "https://spotifystefan-skliarovv1.p.rapidapi.com/getRecomendationPlaylist"

payload = "accessToken=%3CREQUIRED%3E&seedArtists=%3CREQUIRED%3E&seedGenres=%3CREQUIRED%3E&seedTracks=%3CREQUIRED%3E"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "01fa109a82msh56c6f743bd1a72ap1b7e10jsn5dc27a7edb92",
    'x-rapidapi-host': "Spotifystefan-skliarovV1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)