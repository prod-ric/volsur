import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

def generate_sample_vol_data(n_strikes=20, n_tenors=10):
    """Generate sample volatility data."""
    # Create strikes (70% to 130% of current price)
    spot = 100
    strikes = np.linspace(0.7 * spot, 1.3 * spot, n_strikes)
    
    # Create tenors (1M to 2Y)
    tenors = np.linspace(1/12, 2, n_tenors)
    
    # Create volatility surface with smile effect and term structure
    vols = np.zeros((len(strikes), len(tenors)))
    for i, k in enumerate(strikes):
        for j, t in enumerate(tenors):
            # Basic volatility smile
            moneyness = k/spot
            smile = 0.2 + 0.1 * (moneyness - 1)**2
            # Term structure effect
            term = 0.05 * np.log(t + 0.5)
            # Combine effects
            vols[i, j] = smile + term
            
    return strikes, tenors, vols

def plot_vol_surface(strikes, tenors, vols):
    """Create 3D surface plot using plotly."""
    X, Y = np.meshgrid(tenors, strikes)
    
    fig = go.Figure(data=[go.Surface(x=X, y=Y, z=vols)])
    
    fig.update_layout(
        title='Implied Volatility Surface',
        scene = dict(
            xaxis_title='Tenor (Years)',
            yaxis_title='Strike',
            zaxis_title='Implied Volatility'
        ),
        width=800,
        height=800
    )
    
    return fig

def main():
    st.title('Volatility Surface Visualization')
    
    # Sidebar controls
    st.sidebar.header('Parameters')
    n_strikes = st.sidebar.slider('Number of Strikes', 10, 50, 20)
    n_tenors = st.sidebar.slider('Number of Tenors', 5, 20, 10)
    
    # Generate and plot data
    strikes, tenors, vols = generate_sample_vol_data(n_strikes, n_tenors)
    fig = plot_vol_surface(strikes, tenors, vols)
    
    # Display plot
    st.plotly_chart(fig)
    
    # Display data table
    if st.checkbox('Show Raw Data'):
        df = pd.DataFrame(
            vols,
            index=[f'{s:.2f}' for s in strikes],
            columns=[f'{t:.2f}Y' for t in tenors]
        )
        st.write('Volatility Matrix:')
        st.dataframe(df)

if __name__ == '__main__':
    main()