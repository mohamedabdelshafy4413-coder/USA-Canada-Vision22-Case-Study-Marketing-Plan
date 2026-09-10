import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vision22 USA Canada Growth Intelligence', page_icon='🌎', layout='wide')

st.title('🌎 USA & Canada Vision22 Growth Intelligence Hub')
st.subheader('B2B Digital Marketing Strategy, Sales Intelligence & Revenue Platform')

menu = st.sidebar.selectbox('Navigation',[
    'Executive Dashboard',
    'Industry Intelligence',
    'Lead Scoring Engine',
    'Service Packages',
    'Revenue Forecast',
    'Sales Pipeline',
    'Market Intelligence'
])

if menu == 'Executive Dashboard':
    st.header('Executive Dashboard')
    c1,c2,c3,c4=st.columns(4)
    c1.metric('Target Market','USA + Canada')
    c2.metric('Priority Industries',5)
    c3.metric('Avg Retainer','$10K-$25K')
    c4.metric('90 Day Goal','First 5-10 Clients')

    st.write('Vision22 positioning: Full-service B2B Growth Partner for companies seeking qualified opportunities and predictable sales pipelines.')

elif menu == 'Industry Intelligence':
    st.header('Priority B2B Industries')
    df=pd.DataFrame([
        ['Manufacturing','$8K-$30K/mo','Lead Generation + SEO + Expansion'],
        ['Construction','$7K-$25K/mo','Ads + Conversion + Pipeline'],
        ['B2B SaaS','$10K-$40K/mo','Demand Generation + LinkedIn'],
        ['Distribution','$8K-$25K/mo','Buyer Acquisition'],
        ['Professional Services','$5K-$15K/mo','Authority + Content']
    ],columns=['Industry','Value','Recommended Solution'])
    st.dataframe(df,use_container_width=True)

elif menu == 'Lead Scoring Engine':
    st.header('Company Opportunity Score')
    employees=st.slider('Employees',1,2000,100)
    website=st.checkbox('Strong Website')
    marketing=st.checkbox('Existing Marketing Team')
    score=50
    if employees>100: score+=20
    if not website: score+=15
    if not marketing: score+=15
    st.metric('Opportunity Score',f'{score}/100')
    if score>=80:
        st.success('High Priority Prospect')

elif menu == 'Service Packages':
    st.header('Premium B2B Packages')
    packages=[
        ['Complete B2B Marketing Department','$15K-$50K/month'],
        ['B2B Performance Growth System','$8K-$30K/month'],
        ['B2B Lead Generation Engine','$7K-$20K/month'],
        ['International B2B Expansion','$10K-$35K/project'],
        ['Digital Authority System','$5K-$20K/month'],
        ['Website & Conversion System','$10K-$50K/project'],
        ['Growth Foundation','$5K-$10K/project']]
    st.table(pd.DataFrame(packages,columns=['Package','Price']))

elif menu == 'Revenue Forecast':
    st.header('Revenue Forecast Model')
    companies=st.number_input('Target Companies',100,100000,5000)
    reply=st.slider('Positive Reply %',1,20,5)
    close=st.slider('Closing %',1,50,15)
    retainer=st.number_input('Average Retainer',5000,50000,10000)
    clients=(companies*reply/100)*(close/100)
    revenue=clients*retainer
    a,b=st.columns(2)
    a.metric('Expected Clients',round(clients,1))
    b.metric('Monthly Revenue',f'${revenue:,.0f}')

elif menu == 'Sales Pipeline':
    st.header('B2B Sales Pipeline')
    stages=['Prospects','Contacted','Replies','Meetings','Proposals','Won Clients']
    for s in stages:
        st.write('➡️',s)

elif menu == 'Market Intelligence':
    st.header('USA & Canada Marketing Intelligence')
    st.write('Future modules: Google Ads updates, SEO trends, LinkedIn B2B changes, competitor monitoring and market opportunities.')

st.success('Vision22 Growth Intelligence Platform V4 Ready')
