import streamlit as st
import websocket


def show_websocket_test():

    st.title("WebSocket Test")

    message = st.text_input(
        "Enter message"
    )

    if st.button("Send"):

        ws = websocket.WebSocket()

        ws.connect(
            "ws://127.0.0.1:8000/ws"
        )

        ws.send(message)

        result = ws.recv()

        st.success(result)

        ws.close()