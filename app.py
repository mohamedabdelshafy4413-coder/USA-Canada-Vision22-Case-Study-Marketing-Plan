import streamlit as st
import pandas as pd

st.set_page_config(page_title='USA Canada Vision22 Growth Plan', layout='wide')

st.title('USA & Canada Vision22 Case Study & Marketing Plan')
st.subheader('B2B Digital Growth Intelligence Dashboard')

st.info('Strategic dashboard for B2B digital marketing expansion in USA and Canada')

industries = pd.DataFrame([
    ['Manufacturing','$8K-$30K/mo','Lead Generation + SEO + International Growth'],
    ['Construction','$7K-$25K/mo','Lead Generation + Ads + Conversion'],
    ['B2B SaaS','$10K-$40K/mo','Demand Generation + SEO + LinkedIn'],
    ['Distribution','$8K-$25K/mo','Buyer Acquisition + Email Campaigns']
],columns=['Industry','Expected Value','Recommended Services'])

st.header('Target Industries')
st.dataframe(industries,use_container_width=True)

st.header('Vision22 Premium Packages')
packages=[
'Complete B2B Marketing Department',
'B2B Performance Growth System',
'B2B Lead Generation Engine',
'International B2B Expansion System',
'B2B Digital Authority System',
'Website & Conversion System',
'B2B Growth Foundation'
]

for p in packages:
    st.success(p)

st.header('90 Day Market Entry Plan')
st.write('Target companies, run email campaigns, generate meetings, and convert retainers.')
