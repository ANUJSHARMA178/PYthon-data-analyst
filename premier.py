import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load():
    return pd.read_csv('premierleague.csv')

# main load starts here
df = load()

with st.expander('View raw premier league data'):
    st.dataframe(df.sample(1000))

rows,cols = df.shape
c1,c2 = st.columns(2)
c1.markdown(f'### total Records : {rows}')
c1.markdown(f'### total columns : {cols}')

numeric_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(exclude=['number'])
with st.expander("Columns names"):
  st.markdown(f'Columns with numbers : {",".join(numeric_df)}')
  st.markdown(f'Columns without numbers : {",".join(cat_df)}')

  # visualization 

c1,c2 = st.columns([1,2])
xcol = c1.selectbox("choose a column for x-axis", numeric_df.columns)
ycol = c1.selectbox("choose a column for y-axis", numeric_df.columns)
zcol = c1.selectbox("choose a column for z-axis", numeric_df.columns)
color = c1.selectbox("choose a column for color", cat_df.columns)
fig = px.scatter_3d(df, x=xcol,y=ycol,z=zcol,color=color)
c2.plotly_chart(fig,use_container_width=True)