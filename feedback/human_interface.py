import streamlit as st
from feedback.rl_reward import update_rewards
from storage.chroma_store import store_version

def run_human_loop(original, spun, reviewed, chapter_id, version):
    st.title("AI Book Chapter Review")
    st.subheader("Original Chapter")
    st.text_area("Original", original, height=200)

    st.subheader("AI Writer Output")
    st.text_area("Spun Text", spun, height=200)

    st.subheader("AI Reviewer Output")
    final_text = st.text_area("Reviewed Text", reviewed, height=200)

    rating = st.slider("Rate this version", 0, 10, 5)
    if st.button("Submit Rating"):
        store_version(chapter_id, version, final_text, score=rating)
        update_rewards(chapter_id, version, rating)
        st.success("Thanks for your feedback!")