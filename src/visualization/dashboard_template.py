import feather
import matplotlib
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
import pandas as pd
import pickle

html_header="""
<head>
<title>Predictive Maintenance</title>
<meta charset="utf-8">
<meta name="keywords" content="turbofan prognostics, dashboard, predictive maintenance">
<meta name="description" content="turbofan prognostic dashboard">
<meta name="author" content="Team prognostics">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#008080; font-family:Georgia"> Turbofan Prognostics <br>
 <h2 style="color:#008080; font-family:Georgia"> DASHBOARD</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""
st.set_page_config(page_title="Turbofan Prognostics Dashboard", page_icon="", layout="wide")
st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

### data import #########################################################################################
data_path = "data"
data=pd.read_csv('curva.csv')

train = pickle.load( open( f"{data_path}/prognostics_train.p", "rb" ) )

### Block 1#########################################################################################
html_card_header1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 450px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Fleet average remaining useful life</h3>
  </div>
</div>
"""
k=555
html_card_footer1=f"""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 450px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Previous {k}</p>
  </div>
</div>
"""
k21=2
html_card_header2=f"""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 450px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Number of alerts on Operational setting{k21}</h3>
  </div>
</div>
"""
k22 = 9000
html_card_footer2=f"""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 450px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Previous {k22}</p>
  </div>
</div>
"""
k23 = 11
html_card_header3=f"""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 450px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Number of alerts on Sensor{k23}</h3>
  </div>
</div>
"""
k24 = 25
html_card_footer3=f"""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 450px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Previous {k24}</p>
  </div>
</div>
"""
### 
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,15,1,15,1,15,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header1, unsafe_allow_html=True)
        fig_c1 = go.Figure(go.Indicator(
            mode="number+delta",
            value=35,
            number={"font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
            delta={'position': "bottom", 'reference': -2, 'relative': False},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c1.update_layout(autosize=False,
                             width=450, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#fbfff0", font={'size': 20})
        st.plotly_chart(fig_c1)
        st.markdown(html_card_footer1, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header2, unsafe_allow_html=True)
        fig_c2 = go.Figure(go.Indicator(
            mode="number+delta",
            value=5,
            number={"font": {"size": 40, 'color': "#008080", 'family': "Arial"}, 'valueformat': ',f'},
            delta={'position': "bottom", 'reference': 2},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c2.update_layout(autosize=False,
                             width=450, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#fbfff0", font={'size': 20})
        fig_c2.update_traces(delta_decreasing_color="#3D9970",
                             delta_increasing_color="#FF4136",
                             delta_valueformat='f',
                             selector=dict(type='indicator'))
        st.plotly_chart(fig_c2)
        st.markdown(html_card_footer2, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        st.markdown(html_card_header3, unsafe_allow_html=True)
        fig_c3 = go.Figure(go.Indicator(
            mode="number+delta",
            value=4,
            number={"font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
            delta={'position': "bottom", 'reference': 1, 'relative': True},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c3.update_layout(autosize=False,
                             width=450, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#fbfff0", font={'size': 20})
        fig_c3.update_traces(delta_decreasing_color="#3D9970",
                             delta_increasing_color="#FF4136",
                             delta_valueformat='.3f',
                             selector=dict(type='indicator'))
        st.plotly_chart(fig_c3)
        st.markdown(html_card_footer3, unsafe_allow_html=True)
    with col7:
        st.write("")
html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

# ### Block 2#########################################################################################

with st.beta_container():
    #col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,10,1,10,1,20,1])
    col1, col2, col3, col4, col5 = st.beta_columns([1,20,1,20,1])
    with col1:
        st.write("")
    with col2:

        labels = ['Normal','Alert']
        values = [19, 3]

        # Use `hole` to create a donut-like pie chart
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
 
        fig3.update_layout(title={'text': "Fleet Health Status (Segmentation)", 'x': 0.5}, paper_bgcolor="#fbfff0",
                            plot_bgcolor="#fbfff0", font={'color': "#008080", 'size': 12, 'family': "Georgia"}, height=380,
                            width=720,
                            legend=dict(orientation="h",
                                        yanchor="top",
                                        y=0.99,
                                        xanchor="left",
                                        x=0.01),
                            margin=dict(l=1, r=1, b=1, t=30))
        st.plotly_chart(fig3)         

    with col3:
        st.write("")

    with col4:

        sns.set_style("darkgrid")
        sns.color_palette("tab10")
        fig4 = plt.figure(figsize=(16, 8))
        ax1 = sns.lineplot(x='cycles', y='sensor12', data=train.loc[1], ci=None, label="sensor12", legend=False);
        ax2 = ax1.twinx()
        g2 = sns.lineplot(x='cycles', y='RUL', data=train.loc[1], ci=None, color='black', label="RUL", legend=False);
        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = g2.get_legend_handles_labels()
        ax1.legend(h1+h2, l1+l2, loc=1)
        SMALL_SIZE = 10
        MEDIUM_SIZE = 12
        BIGGER_SIZE = 14

        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title      

        st.pyplot(fig4)
    with col7:
        st.write("")

##
html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_line="""
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<p style="color:Gainsboro; text-align: right;">Team prognostics</p>
"""
st.markdown(html_line, unsafe_allow_html=True)
