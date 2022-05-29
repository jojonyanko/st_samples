# hello
import streamlit as st
st.title("I'm jojonyanko")
st.write("I'm jojonyanko")
st.header("I'm jojonyanko")
st.subheader("I'm jojonyanko")
st.text("I'm jojonyanko")
st.latex("a' \overgroup{abs \Overrightarrow{a}} \widecheck{acb \mathring{abcde}}")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label = "The battle cats mod ver.6"
    data=csv.encode("c:/Users/makoto/MCreatorWorkspaces/the_battle_cats_mod/build/reobfJar/The battle cats mod ver.6(new).jar")
    file_name = "The battle cats mod ver.6"
    mime='text/csv'
)