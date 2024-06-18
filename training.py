import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

DATA_PATH = './data.csv'


try:
    # Load the data
    data = pd.read_csv(DATA_PATH)
    print('Data loaded successfully')
    print(data.head())
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print('An error occurred:', e)