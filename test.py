import streamlit as st
import time

st.header("Escolha seu primeiro pokemon!")
selecao = st.selectbox("Escolha seu primeiro pokemon!", ['Charmander', 'Bulbassaur','Squirtle'])
pedra = st.selectbox('Voce tem alguma pedra de evolução?', ['não', 'sim' ] )
my_bar= st.progress(0)
if pedra == 'sim':
    st.write('seu pokemon esta evoluindo!')
    for x in range(100):
        time.sleep(0.1)
        my_bar.progress(x + 1)
    if my_bar.progress(100):
        if selecao == 'Charmander':
            st.image('charmeleon.gif')
        elif selecao == 'Bulbassaur':
            st.image('ivysaur.gif')
        elif selecao == 'Squirtle':
            st.image('wartortle.gif')
    
elif pedra == 'não':
    st.write('Aqui esta seu pokemon!')
    if selecao == 'Charmander':
        st.image('charmander.gif')
    elif selecao == 'Bulbassaur':
        st.image('bulbassaur.gif')
    elif selecao == 'Squirtle':
        st.image('squirtle.gif')
        
