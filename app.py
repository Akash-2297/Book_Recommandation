import pandas as pd
import streamlit as st
import pickle

import pandas


def bookRecom(name):
    book_list=[]
    book_id=book_name[book_name['title']==name].index
    book_id=book_id[0]
    for new in idlist[book_id]:
        book_list.append(book_name.loc[new].title)
    return book_list


book_title=pickle.load(open('book.pkl','rb'))
idlist=pickle.load(open('idlist.pkl','rb'))
book_name=pd.DataFrame(book_title)

st.title("Book Recomandation System")

bn=st.selectbox("Select book name",book_name['title'].values)

if st.button('recomend'):
    recomandation= bookRecom(bn)
    for i in recomandation:
        st.write(i)

