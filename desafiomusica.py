import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_CLIENT_ID = "proibido"
SPOTIFY_CLIENT_SECRET = "proibido"
SPOTIFY_REDIRECT_URI = "proibido"

st.set_page_config(
    page_title="Músicas mais tocadas pela Billboard por data",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Músicas mais tocadas pela Billboard por data ")
st.write("Crie playlists do Spotify a partir das paradas históricas da Billboard Hot 100.")

selected_date = st.date_input(
    "Selecione uma data",
    min_value=datetime(1958, 8, 4).date(),  # Primeira parada Hot 100
    max_value=datetime.now().date(),
    value=datetime.now().date()
)

def fetch_billboard_chart(date):
    """Busca a parada Billboard Hot 100 para uma data específica."""
    url = f"https://www.billboard.com/charts/hot-100/{date.strftime('%Y-%m-%d')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        songs = []
        for item in soup.select(".chart-results-list .o-chart-results-list-row"):
            title = item.select_one(".c-title").text.strip()
            artist = item.select_one(".c-label").text.strip()
            songs.append({"title": title, "artist": artist})
            
        return songs
    except Exception as e:
        st.error(f"Erro ao buscar a parada Billboard: {str(e)}")
        return None
if selected_date:
    with st.spinner("Buscando a parada Billboard Hot 100..."):
        songs = fetch_billboard_chart(selected_date)
        
    if songs:
        st.subheader(f"Billboard Hot 100 - {selected_date.strftime('%d de %B, %Y')}")
        
        for i, song in enumerate(songs, 1):
            with st.container():
                col1, col2 = st.columns([1, 6])
                with col1:
                    st.write(f"#{i}")
                with col2:
                    st.write(f"**{song['title']}**")
                    st.write(f"*{song['artist']}*")
                st.divider()
        
        if st.button("Criar Playlist no Spotify", type="primary"):
            try:
                sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                    client_id=SPOTIFY_CLIENT_ID,
                    client_secret=SPOTIFY_CLIENT_SECRET,
                    redirect_uri=SPOTIFY_REDIRECT_URI,
                    scope="playlist-modify-public"
                ))
                
             
                playlist_name = f"Billboard Hot 100 - {selected_date.strftime('%d de %B, %Y')}"
                user_id = sp.me()["id"]
                playlist = sp.user_playlist_create(user_id, playlist_name, description="Criada com o Billboard Charts Time Machine")
                
             
                track_ids = []
                for song in songs:
                    query = f"track:{song['title']} artist:{song['artist']}"
                    result = sp.search(query, type="track", limit=1)
                    if result["tracks"]["items"]:
                        track_ids.append(result["tracks"]["items"][0]["id"])
                
                if track_ids:
                    sp.playlist_add_items(playlist["id"], track_ids)
                    playlist_url = playlist["external_urls"]["spotify"]
                    st.success(f"✅ Playlist criada com sucesso!")
                    
                    st.markdown(f"[🎵 Abrir Playlist no Spotify]({playlist_url})", unsafe_allow_html=True)
                else:
                    st.warning("Nenhuma música encontrada no Spotify")
                    
            except Exception as e:
                st.error(f"Erro ao criar a playlist no Spotify: {str(e)}")

