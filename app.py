import streamlit as st
import pandas as pd

st.set_page_config(page_title='USA Canada Vision22 Growth Intelligence Hub', page_icon='🌎', layout='wide')

st.title('🌎 USA & Canada Vision22 Growth Intelligence Hub')
st.subheader('B2B Digital Marketing Strategy, Sales Intelligence & Market Entry Platform')

module = st.sidebar.selectbox('Platform Modules',[
'Executive Dashboard','Market Targeting','Prospect Scoring','Service Packages','Revenue Forecast','Email Engine','90 Day GTM Plan'
])

industries=pd.DataFrame([
['Manufacturing','$8K-$30K/mo','Lead Generation + SEO + Expansion'],
['Construction & Engineering','$7K-$25K/mo','Lead Generation + Ads + Conversion'],
['B2B SaaS','$10K-$40K/mo','Demand Generation + SEO + LinkedIn'],
['Distribution','$8K-$25K/mo','Buyer Acquisition + Email'],
['Professional Services','$5K-$15K/mo','Authority + Content']
],columns=['Industry','Value','Recommended Solution'])

packages=pd.DataFrame([
['Complete B2B Marketing Department','$15K-$50K/month'],
['B2B Performance Growth System','$8K-$30K/month'],
['B2B Lead Generation Engine','$7K-$20K/month'],
['International B2B Expansion System','$10K-$35K/project'],
['B2B Digital Authority System','$5K-$20K/month'],
['Website & Conversion System','$10K-$50K/project'],
['B2B Growth Foundation','$5K-$10K/project']
],columns=['Package','Investment'])

if module=='Executive Dashboard':
    a,b,c,d=st.columns(4)
    a.metric('Markets','USA + Canada'); b.metric('Industries','5 Priority'); c.metric('Retainers','$7K-$50K'); d.metric('Goal','5 Clients / 90 Days')
    st.info('Strategic operating system for Vision22 international B2B growth.')

elif module=='Market Targeting':
    st.dataframe(industries,use_container_width=True)
    st.write('Priority regions: Texas, Florida, California, Illinois, Ontario, Alberta, British Columbia')

elif module=='Prospect Scoring':
    employees=st.slider('Company Employees',1,2000,100)
    weak_site=st.checkbox('Website needs improvement')
    no_marketing=st.checkbox('No internal marketing team')
    score=50+(20 if employees>50 else 0)+(15 if weak_site else 0)+(15 if no_marketing else 0)
    st.metric('Opportunity Score',f'{score}/100')
    if score>=80: st.success('High priority account')

elif module=='Service Packages':
    st.dataframe(packages,use_container_width=True)

elif module=='Revenue Forecast':
    companies=st.number_input('Target Companies',100,100000,5000)
    reply=st.slider('Positive Reply %',1,20,5)
    close=st.slider('Closing %',1,50,15)
    value=st.number_input('Average Retainer',5000,50000,10000)
    clients=(companies*reply/100)*close/100
    st.metric('Expected Clients',round(clients,1))
    st.metric('Potential MRR',f'${clients*value:,.0f}')

elif module=='Email Engine':
    st.code('Subject: Growth Opportunity For [Company Name]\n\nWe help B2B companies generate qualified opportunities through digital growth systems.\n\nOpen to a 15-minute discussion?')

elif module=='90 Day GTM Plan':
    st.write('Month 1: Research, ICP, account list, campaign preparation')
    st.write('Month 2: Outreach, meetings, audits and proposals')
    st.write('Month 3: Closing retainers and scaling channels')

st.success('Vision22 Growth Intelligence Platform Ready')