import streamlit as st
import pandas as pd

# Dicionário com os links das playlists do Spotify
SPOTIFY_PLAYLISTS = {
    1980: "https://open.spotify.com/playlist/6oZ2DN1PAnXTvNrxaN91Bw",
    1981: "https://open.spotify.com/playlist/5NOpXpo7eO3w9bz61Cddrn",
    1982: "https://open.spotify.com/playlist/5BFtTmERBsZXIDXoGndTEo",
    1983: "https://open.spotify.com/playlist/3cFgymM4FFOEVjzFti1uBg",
    1984: "https://open.spotify.com/playlist/5VX4jGWx787SCKhjNb4JET",
    1985: "https://open.spotify.com/playlist/0rWDAl8oy1wmpwNAMy7VeY",
    1986: "https://open.spotify.com/playlist/5RTKLkjZVnVGY75oMNO9oe",
    1987: "https://open.spotify.com/playlist/41H2S1Fta7eEaouvhSKjhB",
    1988: "https://open.spotify.com/playlist/7kbt3HAHtK0TuT4oQSDnAt",
    1989: "https://open.spotify.com/playlist/27Aoxq0ufxPFDkxb5jVV9D",
    1990: "https://open.spotify.com/playlist/3oRxIzQGcy632EA0uODFkN",
    1991: "https://open.spotify.com/playlist/6i3zXQMili2gNWa3Sf0QLh",
    1992: "https://open.spotify.com/playlist/1n41TdPdCgphiYq5tp2NzM",
    1993: "https://open.spotify.com/playlist/7hFdmsbb9YCKUre0PQnmBS",
    1994: "https://open.spotify.com/playlist/6n9maiusARsruGCU2FRhjG",
    1995: "https://open.spotify.com/playlist/4rgV7hZ8wKgRvWOGciq8dF",
    1996: "https://open.spotify.com/playlist/6Q6ibEabHgs84xkiyQC3j4",
    1997: "https://open.spotify.com/playlist/2KDN4Ysv00DLlIHoilQJfw",
    1998: "https://open.spotify.com/playlist/0jP80HpSxy7D4yYxd7T0dj",
    1999: "https://open.spotify.com/playlist/2zyyOSJ1OtIyeTbaGQwAZy",
    2000: "https://open.spotify.com/playlist/3gB9aNl2ECGJeRQq0mtITH",
    2001: "https://open.spotify.com/playlist/4EB1D9mHKItRdxHGrs67Tc",
    2002: "https://open.spotify.com/playlist/5bbN3vhAiZqHO3O6UGUqpf"
}

# Configuração da interface no Streamlit
st.title("🎵 Billboard Top Songs (1980-2002)")

# Filtro de ano e mês
anos = list(range(1980, 2003))
meses = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

ano_selecionado = st.selectbox("Selecione o Ano", anos)
mes_selecionado = st.selectbox("Selecione o Mês", meses)

# Exibir botão para acessar a playlist do Spotify do ano selecionado
if ano_selecionado in SPOTIFY_PLAYLISTS:
    st.markdown(f"[🎧 Ouça a playlist com as musicas mais tocados no ano {ano_selecionado} no Spotify]({SPOTIFY_PLAYLISTS[ano_selecionado]})")
else:
    st.write("❌ Nenhuma playlist encontrada para este ano.")



