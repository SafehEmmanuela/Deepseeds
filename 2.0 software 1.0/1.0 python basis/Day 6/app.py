import streamlit as st 
# st.title("Welcome to GenAI fronted")
# st.subheader("Thanks for attending")
# st.subheader("My name is Safeh Emmanuela")
# st.write({
#     "name": "Emma",
#     "age": 19,
#     "School": "Coltech"
# })

from profile import mark_code
print(("run"))
pressed= st.button("Click me")
pressed2= st.button("Click me 2")

st.title("My journey as a genAI frontend developer")
st.header("I am a beginner")
st.subheader("I will love to take y'all along")
st.markdown(mark_code) 
st.image("IMG-20240414-WA0002.jpg", caption= "Aspiring AI engineers", use_container_width=True)


def creating_form():
    with st.form (key="form_submit"):
        name=st.text_input("Input your username")
        email=st.text_input("Input your email")
        school=st.text_input("Input your school")
        number=st.text_input("Input your number")
        description= st.text_area(label="please tell us more about you")
        submit=st.form_submit_button(label="submit info")

        if submit:
            if name and email and school and number and description:
                st.success("Thank you for submitting")
                st.balloons()
                return{
                    "name": name,
                    "email":email,
                    "number":number,
                    "school":school,
                    "description":description
                    }
            else:
                st.error("please fill all the forms")

data=creating_form()
print(f"My data is {data}")

# creating side bars
st.sidebar.title("navigation")
name= st.sidebar.text_input("Enter your name")
age= st.sidebar.slider("Select your age", 0,100)
temp= st.sidebar.slider("Creativity", 0.0, 1.0,0.7)
model_choice= st.sidebar.selectbox("Model", ["GPT-4", "Claude", "GEnAi"])
st.write(f"Hello your are {name}, and you are {age} years old")


import time
progress= st.progress(0)

for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.success("✅ Generation complete")


# 2. Tabs(st.tabs)
# Separate content into multiple pages without navigating

tab1, tab2= st.tabs(["✍️ Prompt", "📃 Ouput"])
with tab1:
    st.text_area("Enter your prompt")
with tab2:
    st.write("Generated result appears here")



# 3. Columns (st.columns)
# Place elements side by side (e.g, Inputs ont the left, results on the right)

col1, col2 =st.columns(2)

with col1:
    st.text_input("Enter Prompts")

    with col2:
        st.write("AI result goes here")

# 4. Container (st.container)
# Group related elements and allow for dynamic updates inside the group.

container= st.container()

container.write("GEnerated Text Area")
btn= container.button("Generate Text")


# 5. Expander (st.expander)
# Hide/show details on demand - useful for advanced sttings or explanations

with st.expander("Advanced Options"):
    st.slider("Max Tokens",100,1000)
    st.checkbox("Stream Output")


# 6. Empty (st.empty)
# Reserve a space for content that updates later (e.g, dynamic result areas)

placeholder = st.empty()

if st.button("Generate"):
    placeholder.write("🔁Generating...")
    # simulate generation
    placeholder.write("✅Done! Here's the result.")


# combine layouts for a GenAI App

import streamlit as st
st.title("🧠 GenAI Prompt GEnerator")
# sidebar settings
temp= st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# Tabs
tab1, tab2= st.tabs(["📝Prompt", "📃 Ouput"])
with tab1:
    prompt=st.text_area("Enter your prompt")
with tab2:
    st.write("**AI Output:**")
    if st.button("Generate"):
        st.success(f"Response from model (temp={temp} for: {prompt})")
