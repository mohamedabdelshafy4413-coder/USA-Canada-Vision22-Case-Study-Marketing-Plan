import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vision22 North America Growth OS', page_icon='🌎', layout='wide')

st.title('🌎 Vision22 North America B2B Growth OS')
st.caption('USA & Canada Market Strategy | Buyer Intelligence | Sales Pipeline | Revenue Command Center')

with st.sidebar:
    module = st.selectbox('Command Center',[
        'Executive Dashboard','Market Strategy','ICP Builder','Buyer Scoring','Package Engine','Revenue Forecast','Sales Pipeline','Marketing Plan'
    ])

industries = pd.DataFrame([
['Manufacturing','★★★★★','$8K-$30K/mo','Lead Generation + SEO + Expansion'],
['Construction & Engineering','★★★★★','$7K-$25K/mo','Pipeline + Ads + Conversion'],
['B2B SaaS','★★★★★','$10K-$40K/mo','Demand Generation + LinkedIn'],
['Distribution','★★★★','$8K-$25K/mo','Buyer Acquisition'],
['Professional Services','★★★★','$5K-$15K/mo','Authority + Content']
],columns=['Industry','Opportunity','Retainer','Growth System'])

if module=='Executive Dashboard':
    st.header('Executive Growth Dashboard')
    c1,c2,c3,c4=st.columns(4)
    c1.metric('Markets','USA + Canada')
    c2.metric('Priority Industries','5')
    c3.metric('Target Retainer','$10K-$50K')
    c4.metric('90 Day Goal','5-10 Clients')
    st.dataframe(industries,use_container_width=True)

elif module=='Market Strategy':
    st.header('USA & Canada Market Strategy')
    st.subheader('USA Priority States')
    st.write('Texas | California | Illinois | North Carolina | Florida')
    st.subheader('Canada Priority Provinces')
    st.write('Ontario | Alberta | British Columbia')

elif module=='ICP Builder':
    st.header('Ideal Customer Profile Builder')
    industry=st.selectbox('Select Industry',industries['Industry'])
    st.success(f'{industry} selected')
    st.write('Decision Makers: CEO | Founder | VP Sales | Marketing Director | Business Development')

elif module=='Buyer Scoring':
    st.header('Buyer Opportunity Score')
    employees=st.slider('Employees',1,5000,200)
    website=st.checkbox('Strong Website')
    marketing=st.checkbox('Marketing Team')
    score=50+(20 if employees>100 else 0)+(15 if not website else 0)+(15 if not marketing else 0)
    st.metric('Opportunity Score',f'{score}/100')
    st.write('A+ Priority Prospect' if score>=80 else 'Qualified Prospect')

elif module=='Package Engine':
    st.header('Growth Package Recommendation')
    problem=st.selectbox('Business Challenge',['Need Leads','Weak Digital Presence','Need Authority','International Expansion'])
    packages={'Need Leads':'B2B Lead Generation Engine ($7K-$20K/mo)','Weak Digital Presence':'Website & Conversion System ($10K-$50K)','Need Authority':'Digital Authority System ($5K-$20K/mo)','International Expansion':'International B2B Expansion ($10K-$35K)'}
    st.success(packages[problem])

elif module=='Revenue Forecast':
    st.header('Revenue Forecast Model')
    accounts=st.number_input('Target Accounts',100,100000,10000)
    reply=st.slider('Reply Rate %',1,20,5)
    close=st.slider('Close Rate %',1,50,15)
    retainer=st.number_input('Average Retainer',5000,50000,12000)
    clients=accounts*reply/100*close/100
    a,b=st.columns(2)
    a.metric('Expected Clients',round(clients))
    b.metric('Monthly Revenue',f'${clients*retainer:,.0f}')

elif module=='Sales Pipeline':
    st.header('Sales Pipeline Command Center')
    pipeline=pd.DataFrame({'Stage':['Prospects','Contacted','Replies','Meetings','Proposals','Won'],'Count':[10000,1500,200,50,15,5]})
    st.bar_chart(pipeline.set_index('Stage'))
    st.dataframe(pipeline,use_container_width=True)

elif module=='Marketing Plan':
    st.header('90 Day Marketing Execution Plan')
    st.write('Month 1: ICP + Database + Campaign Setup')
    st.write('Month 2: Outreach + Meetings + Optimization')
    st.write('Month 3: Closing + Retainers + Scaling')

st.success('Vision22 North America Growth OS V6 Active')