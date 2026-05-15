import streamlit as st
import requests


def show_login():

    left, center, right = st.columns([1,2,1])

    with center:

        st.markdown("")

        st.markdown("")

        st.title("Enterprise Login")

        st.caption(
            "Secure Employee Management Portal"
        )

        st.markdown("---")

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        st.markdown("")

        if st.button("Login"):

            try:

                response = requests.post(

                    "http://127.0.0.1:8000/login",

                    data={

                        "username": username,

                        "password": password
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state["token"] = (
                        data["access_token"]
                    )

                    st.session_state[
                        "logged_in"
                    ] = True

                    st.success(
                        "Login successful"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid credentials"
                    )

            except Exception as e:

                st.error(f"Error: {e}")


def logout():

    st.session_state.clear()

    st.success(
        "Logged out successfully"
    )

    st.rerun()