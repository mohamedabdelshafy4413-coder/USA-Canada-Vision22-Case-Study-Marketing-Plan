import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vision22 North America Growth OS', page_icon='🌎', layout='wide')

st.title('🌎 Vision22 North America B2B Growth OS')
st.caption('USA & Canada Market Intelligence | Sales Engine | Revenue Planning Platform')

menu = st.sidebar.selectbox('Modules',[
    'Executive Dashboard',
    'ICP & Industry Selector',
    'Lead Scoring Engine',
    'Package Recommendation',
    'Revenue Simulator',
    'CRM Pipeline',
    'Market Intelligence'
])

industries={
'Manufacturing':'High Value | $8K-$30K/mo','Construction & Engineering':'High Value | $7K-$25K/mo','B2B SaaS':'Premium | $10K-$40K/mo','Distribution':'Growth | $8K-$25K/mo','Professional Services':'Authority | $5K-$15K/mo'}

if menu=='Executive Dashboard':
    st.header('Executive Growth Dashboard')
    a,b,c,d=st.columns(4)
    a.metric('Target Markets','USA + Canada')
    b.metric('Priority Industries','5')
    c.metric('Target Retainer','$10K-$50K')
    d.metric('90 Day Target','5-10 Clients')
    st.info('Vision22 operates as an outsourced B2B marketing department for companies needing predictable growth.')

elif menu=='ICP & Industry Selector':
    st.header('Ideal Customer Profile')
    industry=st.selectbox('Industry',list(industries.keys()))
    st.success(industry+' → '+industries[industry])
    st.write('Buyer Focus: CEO, Founder, VP Sales, Marketing Director, Business Development Manager')

elif menu=='Lead Scoring Engine':
    st.header('Prospect Opportunity Scoring')
    employees=st.slider('Employees',1,5000,200)
    website=st.checkbox('Professional Website')
    marketing=st.checkbox('Internal Marketing Team')
    score=40
    if employees>100: score+=25
    if not website: score+=20
    if not marketing: score+=15
    st.metric('Opportunity Score',str(score)+'/100')
    st.write('A+ Priority' if score>=80 else 'Qualified Prospect')

elif menu=='Package Recommendation':
    st.header('Recommended Growth Solution')
    problem=st.selectbox('Main Challenge',['No Leads','Weak Website Conversion','Low Visibility','Need Market Expansion'])
    mapping={'No Leads':'B2B Lead Generation Engine','Weak Website Conversion':'Website & Conversion System','Low Visibility':'Digital Authority System','Need Market Expansion':'International B2B Expansion System'}
    st.success(mapping[problem])

elif menu=='Revenue Simulator':
    st.header('90 Day Revenue Forecast')
    leads=st.number_input('Target Accounts',100,100000,5000)
    reply=st.slider('Positive Reply %',1,20,5)
    close=st.slider('Closing %',1,50,15)
    value=st.number_input('Average Monthly Retainer',5000,100000,15000)
    clients=leads*reply/100*close/100
    st.metric('Expected Clients',round(clients))
    st.metric('Expected MRR',f'${clients*value:,.0f}')

elif menu=='CRM Pipeline':
    st.header('Sales Pipeline')
    data=pd.DataFrame({'Stage':['Prospects','Contacted','Replies','Meetings','Proposals','Won'],'Count':[5000,800,100,30,10,5]})
    st.dataframe(data,use_container_width=True)

elif menu=='Market Intelligence':
    st.header('USA & Canada Market Intelligence')
    st.write('Future integrations: market feeds, SEO changes, advertising trends, competitor monitoring and industry opportunities.')

st.success('Vision22 Growth OS V5 Active')