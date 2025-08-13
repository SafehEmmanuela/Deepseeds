import streamlit as st 
st.title("💬Chat with DEEPSEED")


st.sidebar.title("🌱DEEPSEED")
st.sidebar.caption("One seed at a time")
st.sidebar.markdown("___")

st.sidebar.subheader("📊 Session statistics")
col1,col2= st.columns(2)
with col1:
    st.sidebar.write("Messages")
    st.sidebar.markdown("# 2")
with col2:
    st.sidebar.write("Total")
    st.sidebar.markdown("# 2")
st.sidebar.markdown("___")

st.sidebar.subheader("🚀Quick action")
st.sidebar.button("💡Tell me a joke")
st.sidebar.button("💡Explain AI")
st.sidebar.button("💡Help brainstorm")
st.sidebar.button("💡Writing tips ")
st.sidebar.button("💡Book recommendation")
st.sidebar.markdown("___")

st.sidebar.subheader("⚙️Control")

st.chat_message("assistance").markdown("🛑Welcome to the world of Deepseed")
st.chat_message("assistance").markdown("🤖🌱Based on your message, I can provide some insights on this")



st.markdown("###")
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Message DEEPSEED:", placeholder="Type your message here...", key="input")
    submit_button = st.form_submit_button("Send🚀")

if submit_button and user_input:
    st.chat_message("user").markdown(user_input)
    st.chat_message("assistant").markdown("🤖 This is a placeholder response from DEEPSEED.")

