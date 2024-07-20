import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from llm_chain import Chain
import os
from modules.process_image import get_image_content
import time
# Function to set a flag indicating that user input has been sent
def sent_input():
    st.session_state.send_input = True

# Function to process the uploaded image and generate a description
def respone_when_use_image(Image_file):
    with st.spinner("I am processing image"):
        # Default prompt for image description
        temp_prompt = "Describe the image for me plz"
        # Use the user's question as the prompt if provided
        if st.session_state.user_question != "":
            temp_prompt = st.session_state.user_question
        return get_image_content(Image_file.getvalue(), temp_prompt)

def main():
    st.set_page_config(
        page_title="Aizen_chatbot",
        page_icon="🐺",
        layout="centered",
    )
    st.title("🤖 Integrated chatbots")
    chat_container = st.container()

    # Initialize session state variables if not already set
    if 'send_input' not in st.session_state:
        st.session_state['send_input'] = False
        st.session_state["user_question"] = ""
        st.session_state["user_input"] = ""
        st.session_state["flag_img_file"] = False

    # Sidebar for uploading files
    st.sidebar.title("Upload your file!")
    Image_file = st.sidebar.file_uploader("Upload Image File", type=["jpg", "jpeg", "png"])



    # Input field for user questions
    st.session_state.user_question = st.chat_input("Enter your question", on_submit=sent_input)
    
    chat_history = StreamlitChatMessageHistory(key="history")
    x = Chain(chat_history=chat_history)
    with chat_container:
        for message in chat_history.messages:
            with st.chat_message(message.type):
                st.markdown(message.content)
    # Handle user input
    if st.session_state.send_input:
        # Process the image if uploaded and not previously processed
        if Image_file and st.session_state.flag_img_file == False:
            st.session_state.flag_img_file = True
            with chat_container:
                with st.chat_message("human"):
                    st.markdown(st.session_state.user_question)
            respone_img = respone_when_use_image(Image_file)
            with chat_container:
                chat_history.add_user_message(st.session_state.user_question)
                chat_history.add_ai_message(respone_img)
                with st.chat_message("ai"):
                    typing_placeholder = st.empty()
                    tmp_str = ""
                    for char in respone_img:
                        tmp_str += char
                        time.sleep(0.01)  
                        typing_placeholder.markdown(tmp_str)
                st.session_state.user_question = ""
                st.session_state.send_input = False


        # Process text input from the user
        if st.session_state.user_question != "":
            with chat_container:
                with st.chat_message("human"):
                    st.markdown(st.session_state.user_question)
                llm_response = x.invoke(user_input=st.session_state.user_question)
                tmp_str = ""
                with st.chat_message("ai"):
                    typing_placeholder = st.empty()
                    for char in llm_response["response"]:
                        tmp_str += char
                        time.sleep(0.01)
                        typing_placeholder.markdown(tmp_str)
                st.session_state.send_input = False
if __name__ == "__main__":
    main()
