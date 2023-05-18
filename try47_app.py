import streamlit as st




st.set_page_config(
    layout='wide',
    page_title='Dash board',


)



page = st.sidebar.radio('Select Page', ['page1', 'page2', 'page3'])
if page=='page1':


    st.title(' Hello,This is Mohamed Shams Dashboard & website ')


    st.header(' i love python')
    #st.dataframe(df)



    btn=st.button('Submit')
    if btn:
        st.info('A7A')

    RD=st.radio('Select',['A','B','C']) 
    if RD=='A':
        st.info(' ايه اللى اخرك يا وحوح')   
    elif RD=='B':
        st.warning(' اه احنا جايين نهزر بقى ')   
    else:
        st.error('يابنى حل عنى الله يرضى عليك ')  



    chk=st.checkbox('I Agree')     
    if chk:
        st.exception('خلى بالك انت داخل على حوارات يا نجم ')

    st.selectbox('select you answer',['xx','yy','zz'])       

    st.slider('select',0,70)
    st.select_slider('select you answer',['X','Y','Z'])
    st.text_area('enter text here')
    st.text_area(' write parhgraf')
    st.file_uploader('Upload your file')
    #st.camera_input('picture')
    st.date_input('today')
    st.time_input('now')
    st.number_input('enter sap number')
    st.multiselect('select you answer',['xx','yy','zz'])
