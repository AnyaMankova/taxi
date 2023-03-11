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


# Делаем визуализацию распределения вызовов в зависимости от дня в месяце
#создаю фигуру, на которой будет располагаться гистограмма
fig = plt.figure(figsize=[12, 6])

# строим гистограмму распределения по дням
# hist самостоятельно подсчитывает кол-во по каждому дню
plt.hist(uber_df['Day'], width= 0.6, bins= 30)
plt.title('Распределение вызовов такси по датам месяца', fontsize=16)
plt.xlabel('День', fontsize=14)
plt.ylabel('Количество вызовов', fontsize=14)

# сохраняем картинку
plt.savefig('Day.png', dpi=120)

#print(uber_df.head(5))