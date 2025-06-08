#Task 3: Interactive Visualizations with Plotly

# Load the Plotly wind datase
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

#Print the first and last 10 lines of the DataFrame
print(df.head(10))
print(df.tail(10))

#Clean the data
#Convert the 'strength' column to a float
#Use of str.replace() with regex is one way to do this, followed by type conversion
df['strength'] = df['strength'].str.replace(r'[^0-9.]+.*', '', regex=True).astype(float)

#Interactive scatter plot of strength vs. frequency, with colors based on the direction
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'}
)

#Save and load the HTML file, as wind.html
fig.write_html("wind.html")