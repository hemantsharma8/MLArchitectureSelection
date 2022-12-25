
import streamlit as st

st.set_page_config(
    page_title="Decision making about architecture to be used in Machine Learning production",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr, .css-qbe2hs {
            background-color:    #154360    !important;
            color: black !important;
        }
        div[role="radiogroup"] {
            color:black !important;
            margin-left:8%;
        }
        div[data-baseweb="select"] > div {
            
            color: black;
        }
        div[data-baseweb="base-input"] > div {
            background-color: #aab7b8 !important;
            color: black;
        }
        
        .st-cb, .st-bq, .st-aj, .st-c0{
            color: black !important;
        }
        .st-bs, .st-ez, .st-eq, .st-ep, .st-bd, .st-e2, .st-ea, .st-g9, .st-g8, .st-dh, .st-c0 {
            color: black !important;
        }
        .st-fg, .st-fi {
            background-color: #c6703b !important;
            color: black !important;
        }
        
        .st-g0 {
            border-bottom-color: #c6703b !important;
        }
        .st-fz {
            border-top-color: #c6703b !important;
        }
        .st-fy {
            border-right-color: #c6703b !important;
        }
        .st-fx {
            border-left-color: #c6703b !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown('<h1 style="margin-left:8%; color:#FA8072">Software Architecture Selection</h1>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("About", "Architecture selection")
)

if add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')
    st.markdown('Here are some important considerations while choosing an architecture',unsafe_allow_html=True)
    st.markdown('<h3>Modularity:</h3> The code used in preprocessing/feature engineering should be arranged in comprehensive pipelines. ',unsafe_allow_html=True)
    st.markdown('<h3>Reproducibility:</h3> The output of each component must be replicable for any version in time.',unsafe_allow_html=True)
    st.markdown('<h3>Scalability:</h3> The model must be servable to a large number of customers with minimal response time.',unsafe_allow_html=True)
    st.markdown('<h3>Extensibility:</h3> It should be easy to modify for future tasks.',unsafe_allow_html=True)
    st.markdown('<h3>Testing:</h3> The ability to test variation between model versions. ',unsafe_allow_html=True)
    st.markdown('<h3>Automation:</h3> Eliminating manual steps wherever possible to reduce error chances.',unsafe_allow_html=True)
    st.markdown('In this tool we use different scenarios to capture the Non-Functional requirements and chose the optimal architecture',unsafe_allow_html=True)
    
elif add_selectbox == 'Architecture selection':
	
      st.subheader('Architecture to deploy Machine Learning model')
      st.markdown('<h3>Training:</h3>',unsafe_allow_html=True)
      training_weight= st.number_input("Enter the weight you want to give for training:", min_value=0.00, max_value=1.00, step=0.01)
      st.write('You have given ',training_weight,' for Modularity')
      st.markdown('<h3>Prediction:</h3>',unsafe_allow_html=True)
      prediction_weight= st.number_input("Enter the weight you want to give for prediction:", min_value=0.00, max_value=1.00, step=0.01)
      st.write('You have given ',prediction_weight,' for prediction')
      st.markdown('<h3>Prediction result delivery:</h3>',unsafe_allow_html=True)
      prediction_delivery_weight= st.number_input("Enter the weight you want to give for prediction result delivery:", min_value=0.00, max_value=1.00, step=0.01)
      st.write('You have given ',prediction_delivery_weight,' for prediction result delivery')
      st.markdown('<h3>Latency for prediction:</h3>',unsafe_allow_html=True)
      latency_weight= st.number_input("Enter the weight you want to give for latency for prediction:", min_value=0.00, max_value=1.00, step=0.01)
      st.write('You have given ',latency_weight,' for latency for prediction')
      st.markdown('<h3>System Management Difficulty:</h3>',unsafe_allow_html=True)
      management_difficulty_weight= st.number_input("Enter the weight you want to give for automation:", min_value=0.00, max_value=1.00, step=0.01)
      st.write('You have given ',management_difficulty_weight,' for automation')
      submit = st.button('Predict')

      if submit:
            scenario_weights={
                "training":training_weight,
                "prediction":prediction_weight,
                "prediction result delivery":prediction_delivery_weight,
                "latency for prediction":latency_weight,
                "system management difficulty":management_difficulty_weight
            }
            scenario_quality ={
                "training":{
                            "reliability":0.3,
                            "security":0.5,
                            "performance":0.7
                },
                "prediction":{
                            "reliability":0.5,
                            "security":0.5,
                            "performance":0.7
                },
                "prediction result delivery":{
                            "reliability":0.9,
                            "security":0.7,
                            "performance":0.7
                },
                "latency for prediction":{
                            "reliability":0.9,
                            "security":0.3,
                            "performance":0.9
                },
                "system management difficulty":{
                            "reliability":0.7,
                            "security":0.9,
                            "performance":0.4
                }
            }
            AQA ={
                "reliability":0.0,
                "security":0.0,
                "performance":0.0
                }
            qualities = ["reliability","security","performance"]
            for j in scenario_quality.values():
                AQA['reliability']+= j['reliability']
                AQA['security']   += j['security']
                AQA['performance']+= j['performance']
            N=len(scenario_quality)
            for i in AQA:
                AQA[i] = AQA[i]/N
            EWQA ={
                "reliability":0.0,
                "security":0.0,
                "performance":0.0
            }
            for i in scenario_weights:
                x=scenario_weights[i]
                for j in scenario_quality.values():
                    EWQA['reliability']+= x*j['reliability']
                    EWQA['security']   += x*j['security']
                    EWQA['performance']+= x*j['performance']
            QAW ={
                "reliability":0.0,
                "security":0.0,
                "performance":0.0
            }
            for i in QAW:
                QAW[i]=AQA[i]+EWQA[i]
            #quality attribute rank
            quality_quality={
                "reliability":{
                            "performance":0.9,
                            "security":0.9
                },
                "performance":{
                            "reliability":0.9,
                            "security":0.4
                },
                "security":{
                            "reliability":0.5,
                            "performance":0.5
                }
            }
            quality_quality_QAR={
                "reliability":{
                            "performance":0.0,
                            "security":0.0
                },
                "performance":{
                            "reliability":0.0,
                            "security":0.0
                },
                "security":{
                            "reliability":0.0,
                            "performance":0.0
                }
            }
            QAR ={
                "reliability":0.0,
                "performance":0.0,
                "security":0.0
            }
            for i in quality_quality:
                for j in quality_quality[i]:
                    quality_quality_QAR[i][j]+=quality_quality[i][j]*QAW[j]
            for i in QAR:
                QAR[i] = sum(quality_quality_QAR[i].values()) 
            tactics_quality = {"modularity":{
                                            "reliability":0.9,
                                            "security":0.7,
                                            "performance":0.9
                                            },
                                "reproducibility":{
                                             "reliability":0.7,
                                            "security":0.7,
                                            "performance":0.0
                                },
                                "scalability":{
                                             "reliability":0.9,
                                            "security":0.7,
                                            "performance":0.9
                                },
                                "extensibility":{
                                             "reliability":0.7,
                                            "security":0.7,
                                            "performance":0.9
                                },
                                "automation":{
                                             "reliability":0.9,
                                            "security":0.9,
                                            "performance":0.9
                                }
                            }
            tactics_rank={
                            'modularity':0.0,
                            'reproducibility':0.0,
                            'scalability':0.0,
                            'extensibility':0.0,
                            'testing':0.0,
                            'automation':0.0
            }
            for i in tactics_quality:
                for j in QAR:
                    tactics_rank[i] += QAR[j]*tactics_quality[i][j]

    
            style_tactics={
                'REST API':{
                    'modularity':0.7,
                    'reproducibility':0.9,
                    'scalability':0.5,
                    'extensibility':0.9,
                    'testing':0.7,
                    'automation':0.5

                },
                'Shared DB':{
                    'modularity':0.9,
                    'reproducibility':0.7,
                    'scalability':0.5,
                    'extensibility':0.7,
                    'testing':0.5,
                    'automation':0.5
                },
                'Streaming':{
                    'modularity':0.5,
                    'reproducibility':0.5,
                    'scalability':0.9,
                    'extensibility':0.5,
                    'testing':0.9,
                    'automation':0.9
                },
                'Mobile App':{
                    'modularity':0.5,
                    'reproducibility':0.7,
                    'scalability':0.7,
                    'extensibility':0.5,
                    'testing':0.5,
                    'automation':0.7
                }
            }
            architecture_style_rank={
                'REST API':0.0,
                'Shared DB':0.0,
                'Streaming':0.0,
                'Mobile App':0.0
            }
            for i in architecture_style_rank:
                for j in tactics_rank:
                    architecture_style_rank[i]+=style_tactics[i][j]*tactics_rank[j]
            st.write('Hi, ','The architecture scores are ')
            st.write(architecture_style_rank)

