import streamlit as st
import langchain.prompt from PromptTemplate
import langchain_openai from ChatOpenAI

st.title("LLMアプリ")

def AI_query(message,character):
    llm = ChatOpenAI()
    prompt = [
        {"system",f"あなたは週刊少年ジャンプの人気漫画のキャラクター{character}です。ユーザの質問に回答して下さい。"}
        {"user",message}
    ]
    llm.invoke(prompt)

selected_item = st.radio(
    "キャラクターを選択して下さい。",
    ["ルフィ", "ナルト","五条悟"]
)

st.divider()

input_message = st.text_input(label="キャラクターに聞きたいことを入力してね。")

if st.button("聞く"):
    st.divider()    #線

    if input_message:
        answer = AI_query(input_message,selected_item)
    else:
        st.error("質問を入力してね")
