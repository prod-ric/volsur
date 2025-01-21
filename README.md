# Interactive Volatility Surface Visualization

This project provides an interactive 3D visualization of option volatility surfaces using Python. It demonstrates how implied volatility varies across different strike prices and expiration dates, creating the characteristic "volatility smile" pattern observed in options markets.

## Features

The visualization tool offers several key features that make it valuable for understanding options market dynamics:

The interactive surface plot allows users to:
- Rotate and zoom the 3D visualization
- Adjust the number of strike prices and tenor points using slider controls
- View exact volatility values in a complementary heatmap table
- Examine both the volatility smile effect and term structure patterns

## Installation

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/volatility-surface-viz.git
cd volatility-surface-viz
```

This project requires Python 3.7 or later. To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

The requirements.txt file includes:
```
numpy>=1.19.2
pandas>=1.2.0
plotly>=4.14.3
ipywidgets>=7.6.3
jupyter>=1.0.0
```

## Usage

The simplest way to use this visualization is through Jupyter Notebook:

```bash
jupyter notebook
```

Then open the `volatility_surface.ipynb` notebook and run all cells. You'll see:

1. The interactive 3D surface plot
2. Two sliders to control visualization parameters:
   - Number of strike prices (10-50)
   - Number of tenor points (5-20)
3. A DataFrame showing the exact volatility values

### Code Structure

The main components of the visualization are:

`generate_sample_vol_data(n_strikes, n_tenors)`: Creates the volatility surface data with these parameters:
- `n_strikes`: Number of strike prices to generate
- `n_tenors`: Number of expiration dates to generate
- Returns: strikes, tenors, and the volatility matrix

`update_plot(n_strikes, n_tenors)`: Generates and displays the interactive visualization with these features:
- 3D surface plot using Plotly
- Configurable axes and layout
- Complementary DataFrame view of the data

The volatility calculation incorporates both smile and term structure effects:
```python
smile = 0.2 + 0.1 * (moneyness - 1)**2  # Volatility smile component
term = 0.05 * np.log(t + 0.5)           # Term structure component
vol = smile + term                       # Combined effect
```

## Customization

You can modify several aspects of the visualization:

1. Volatility Model Parameters:
   - Base volatility (default: 0.2 or 20%)
   - Smile intensity (default: 0.1)
   - Term structure factor (default: 0.05)

2. Range Parameters:
   - Strike price range (default: ±30% around spot)
   - Tenor range (default: 1 month to 2 years)

3. Visual Elements:
   - Surface color scheme
   - Axis labels and titles
   - Plot dimensions

To modify these, adjust the corresponding parameters in the code:

```python
# Example: Changing the strike price range
strikes = np.linspace(0.5 * spot, 1.5 * spot, n_strikes)  # ±50% around spot

# Example: Modifying the volatility smile intensity
smile = 0.2 + 0.15 * (moneyness - 1)**2  # Increased to 0.15
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Some areas for potential improvement:
- Integration with real market data
- Additional volatility models
- More sophisticated term structure patterns
- Risk metric overlays
- Historical surface comparisons


## Contact

For questions and feedback:
- Email: riccardopansini03@gmail.com
- Twitter: @ric_tvrismo


```
@misc{volatility-surface-viz,
  author = {Riocardo Pansini},
  title = {Interactive Volatility Surface Visualization},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/yourusername/volatility-surface-viz}
}
```
