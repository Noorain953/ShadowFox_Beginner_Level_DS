#MATPLOTLIB

# LINE chart
import matplotlib.pyplot as plt 
import numpy as np 	 
x = np.linspace(0, 10, 100) 
y = np.sin(x) # Create line plot 
plt.figure(figsize=(10, 5)) 
plt.plot(x, y, label='Sine Wave', color='blue') 
plt.title('Line Plot Example') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.legend() 
plt.grid() 
plt.show() 

'''# BAR chart 
categories = ['A', 'B', 'C', 'D'] 
values = [4, 7, 1, 8] # Create bar chart 
plt.figure(figsize=(8, 4)) 
plt.bar(categories, values, color='orange') 
plt.title('Bar Chart Example') 
plt.xlabel('Categories') 
plt.ylabel('Values') 
plt.show() 

# HISTOGRAM 
data = np.random.randn(1000) 
# Create histogram 
plt.figure(figsize=(10, 5)) 
plt.hist(data, bins=30, color='green', alpha=0.7) 
plt.title('Histogram Example') 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.show() 


#SEABORN

# SCATTER plot 
import seaborn as sns 
import pandas as pd 
data = pd.DataFrame({ 
    'x': np.random.rand(100), 
    'y': np.random.rand(100) 
}) 
# Create scatter plot 
plt.figure(figsize=(8, 6)) 
sns.scatterplot(data=data, x='x', y='y', color='purple') 
plt.title('Scatter Plot Example') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.show()

#BOX plot 
data = pd.DataFrame({ 
    'category': ['A']*50 + ['B']*50, 
    'values': np.random.randn(100) 
}) 
# Create box plot 
plt.figure(figsize=(8, 6)) 
sns.boxplot(data=data, x='category', y='values') 
plt.title('Box Plot Example') 
plt.xlabel('Category') 
plt.ylabel('Values') 
plt.show()

# HEATMAP
data = np.random.rand(10, 12) 
# Create heatmap 
plt.figure(figsize=(10, 8)) 
sns.heatmap(data, cmap='coolwarm') 
plt.title('Heatmap Example') 
plt.show() '''

