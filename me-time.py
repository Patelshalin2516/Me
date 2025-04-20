import streamlit as st
import random
import datetime

# Page setup
st.set_page_config(page_title="Pause | A Little Space for You", page_icon="🌿", layout="centered")

# Intro
st.title("🌿 Pause")
st.caption("A quiet space just for you.")

# Name input
name = st.text_input("Hi there. What should I call you?", "Bestie")
st.markdown(f"#### Welcome, {name}. Hope you're finding a little time to breathe today.")

hour = datetime.datetime.now().hour
if hour < 12:
    time_greet = "Good Morning 🌞"
elif 12 <= hour < 17:
    time_greet = "Good Afternoon ☀️"
else:
    time_greet = "Good Evening 🌙"

st.markdown(f"### {time_greet}, {name}!")
# Section: Quote of the Day
quotes = [
    "Have a nice day.",
    "Just keep smiling."
]
st.markdown("A word from the maker")
st.info(random.choice(quotes))

# Section: Mood & Playlist
st.markdown("### 🎧 Your Current Vibe")
moods = {
    "Gujarati": {
        "note": "Some calm for your mind.",
        "link": "https://music.youtube.com/playlist?list=PLevcIXE_BemnlzDRegZSyF0SR6KBLgwt6&si=Xp6RB90nITzJnhdm"
    },
    "Hindi": {
        "note": "Background beats while you conquer the day.",
        "link": "https://music.youtube.com/playlist?list=PLevcIXE_BemlX0Sd4aeEUx9Qyw1DtiXvZ&si=GnBDHPPZEyFWJZ5p"
    },
    "English": {
        "note": "Take a few deep breaths. You got this.",
        "link": "https://music.youtube.com/playlist?list=PLevcIXE_BemnaEVbh1BZj5MUlJDPdXuqp&si=X8hujDTys-Fn1x8H"
    }
}
chosen = st.selectbox("How are you feeling?", list(moods.keys()))
if chosen:
    st.write(moods[chosen]["note"])
    st.markdown(f"[🎵 Open your playlist]({moods[chosen]['link']})")

# Section: One-line Journal
st.markdown("### ✍️ Reflect (Optional)")
today = datetime.date.today().strftime("%B %d, %Y")
with st.form("journal"):
    entry = st.text_input(f"One line for {today} (just for you)")
    submitted = st.form_submit_button("Save it")
    if submitted and entry:
        st.success("Noted. And it stays between you and the screen.")

# Footer
st.markdown("---")
st.caption("This space is always here. Built by someone who cares. 🌿")
