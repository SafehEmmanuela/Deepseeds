import streamlit as st

# if "count" not in st.session_state:
#     st.session_state.count=0

# if st.button("increment"):
#     st.session_state.count +=1
#     st.write(f"count: {st.session_state.count}")

# if "step" not in st.session_state:
#     st.session_state.step=1
# if "info" not in st.session_state:
#     st.session_state.info={}
# def move_to_next():
#     st.session_state.step=2
#     st.session_state.info["name"]=name
# if st.session_state.step==1:
#     st.header("Pleas enter your information")
#     st.write("Trying to be nice")
#     name= st.text_input("Enter your username" ,value= st.session_state.info.get("name"))
#     email= st.text_input("ENter your email")
#     description= st.text_area("Tell us more about yourself")

#     st.button("Next page", on_click= move_to_next(), args= (name,))
#     if next:
#         st.session_state.step=2
#         st.session_state.info["name"]=name
#         st.session_state.info["email"]=email
#         st.session_state.info["description"]=description

# elif st.session_state.step==2:
#     st.header("confirm your information")
#     st.write(f"your information is: {st.session_state.info['name']}")

#     check_box=st.checkbox("confirm information")
#     if check_box:
#         st.balloons()
#     else:
#         prev=st.button("prev")
#         if prev:
#             st.session_state.step=1
            
# call backs
# withoouth callbacks
import streamlit as st
import time

# def expensive_search(query):
#     time.sleep(1) 
#     # simulate heavey work
#     return f"REsult for {query}"
# query= st.text_input("search for something")

# if query:
#     st.write(expensive_search(query))

def expensive_search():
    query= st.session_state.query
    time.sleep(2)
    # simulate heavy work
    st.session_state.results= f"Results for {query}"
st.text_input("search for something", key="query")
st.button("RUn search", on_click=expensive_search)

if "results" in st.session_state:
    st.write(st.session_state.results)