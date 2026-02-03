
import streamlit as st

def main():
    st.title("BRADD Engine")
    st.write("Welcome, sir. BRADD is online and ready to assist.")

    if st.button("Activate BRADD"):
        st.write("BRADD is now active. How may I help you?")

if __name__ == "__main__":
    main()