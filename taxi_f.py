import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg
#from matplotlib.figure import Figure


uber_df = pd.read_csv("uber-raw-data-sep14.csv")
#преобразовываю данные в стандартный формат (изначально было - 9/1/2014)
uber_df['Date/Time'] = pd.to_datetime(uber_df['Date/Time'])

# выделяю отдельно день (дату), час и день недели (в числовом формате от 0 до 6)
uber_df['Day'] = uber_df['Date/Time'].dt.day
uber_df['Hour'] = uber_df['Date/Time'].dt.hour
uber_df['Day_of_week'] = uber_df['Date/Time'].dt.weekday


fig = plt.figure(figsize=[12, 6])
ax = fig.add_subplot()

ax.hist(uber_df['Hour'], bins=24, color= "orange", edgecolor='black')
ax.set_title('Распределение вызовов такси в зависимости от времени суток', fontsize=16)
ax.set_xlabel('Время суток', fontsize=14)
ax.set_xticks([i for i in range(0,24)])
ax.set_ylabel('Количество вызовов', fontsize=14)
plt.savefig('images/Hour.png', dpi=120)

