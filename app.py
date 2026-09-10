import streamlit as st
import pandas as pd

st.set_page_config(page_title='USA Canada Vision22 Growth Platform', layout='wide')

st.title('🌎 USA & Canada Vision22 Case Study & Marketing Plan')
st.subheader('Integrated B2B Digital Growth Intelligence Platform')

st.info('Complete market entry, sales strategy, packages, forecasting and growth dashboard for USA & Canada B2B markets')

# Market Targeting
st.header('🎯 Target Industries')
industries = pd.DataFrame([
['Manufacturing','$8K-$30K/month','Lead Generation, SEO, International Expansion'],
['Construction & Engineering','$7K-$25K/month','Lead Generation, Google Ads, Conversion'],
['B2B SaaS','$10K-$40K/month','Demand Generation, SEO, LinkedIn'],
['Distribution','$8K-$25K/month','Buyer Acquisition, Email Campaigns'],
['Professional Services','$5K-$15K/month','Authority Building, SEO, Content']
],columns=['Industry','Value Range','Growth Solution'])
st.dataframe(industries,use_container_width=True)

# Packages
st.header('📦 Vision22 Premium B2B Packages')
packages=pd.DataFrame([
['Complete B2B Marketing Department','$15K-$50K/month'],
['B2B Performance Growth System','$8K-$30K/month'],
['B2B Lead Generation Engine','$7K-$20K/month'],
['International B2B Expansion System','$10K-$35K/project'],
['B2B Digital Authority System','$5K-$20K/month'],
['Website & Conversion System','$10K-$50K/project'],
['B2B Growth Foundation','$5K-$10K/project']
],columns=['Package','Pricing'])
st.table(packages)

# Case Study
st.header('📘 Vision22 Case Study Framework')
st.write('Positioning: B2B Growth Partner helping companies generate qualified opportunities, improve digital presence and build predictable sales pipelines.')
st.write('Challenges: weak digital visibility, inconsistent lead generation, poor conversion systems and limited authority.')

# Sales Engine
st.header('📧 Sales Outreach Engine')
st.write('Target Account List → Personalized Email Campaign → Meetings → Proposal → Retainer Partnership')

# Revenue Calculator
st.header('💰 Revenue Forecast Calculator')
companies=st.number_input('Target Companies',100,100000,5000)
reply=st.slider('Positive Reply Rate %',1,20,5)
close=st.slider('Closing Rate %',1,50,15)
retainer=st.number_input('Average Monthly Retainer ($)',5000,50000,10000)
meetings=companies*reply/100
clients=meetings*close/100
revenue=clients*retainer
c1,c2,c3=st.columns(3)
c1.metric('Meetings',round(meetings))
c2.metric('Clients',round(clients,1))
c3.metric('Monthly Revenue',f'${revenue:,.0f}')

# Market Intelligence
st.header('📈 Market Intelligence Center')
st.write('Future live module: Google Ads updates, SEO trends, LinkedIn B2B trends, USA/Canada marketing news and competitor intelligence.')

st.success('Vision22 Growth Platform Ready')
