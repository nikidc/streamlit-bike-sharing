SETUP
conda create --name main-ds python=3.11.6
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit

RUN streamlit
streamlit run dashboard.py
streamlit cloud link: