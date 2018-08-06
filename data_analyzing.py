import csv
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd

def print_line(df, x, y, sex, gender):
    color_list = ['lightgray', 'palevioletred', 'lightsalmon', 'lightsteelblue', 'khaki', 'darkseagreen', 'plum']#change color
    for i in range(len(y)):
        if(i % 3 == sex):
            y1 = df.iloc[i,2:7]
            y1 = y1.iloc[::-1]
            plt.plot(x, y1, color=color_list[i//3], linewidth=2.0, linestyle='-', label=y[i])
    leg = plt.legend(loc='best', ncol=2, mode="", shadow=False, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('Suicide rate estimates, crude(' + gender + ')\nEstimates by WHO region\n2000 ~ 2016')
    plt.ylabel('Suicide rate(per 100 000 population)')
    plt.xlabel('Year')
    plt.show()

def print_line_02(df):
    color_list = ['plum', 'orchid', 'mediumorchid', 'darkorchid', 'rebeccapurple']
    label_list = ['0-14', '15-24', '25-44', '45-64', '65-']
    x = range(1994, 2018, 1)
    for i in range(5):
        y1 = df.iloc[0:len(x), i + 1]
        plt.plot(x, y1, color=color_list[i], linewidth = 2.0, linestyle = '-', label = label_list[i])
    leg = plt.legend(loc='best', ncol=2, mode="", shadow=False, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('Suicide rate, Taiwan\n1994 ~ 2017')
    plt.ylabel('Suicide rate(per 100 000 population)')
    plt.xlabel('Year')
    plt.show()
    print(df['25-44'].corr(df['45-64']))

def print_pie(data):
    count_yes = 0
    count_no = 0
    for i in data:
        if(i == 'Yes'):
            count_yes += 1
        elif(i == 'No'):
            count_no += 1
    result = [count_yes, count_no]
    labels = ['Yes', 'No']
    patches, texts, autotexts = plt.pie(result, labels=labels, autopct='%1.1f%%', shadow=False)
    patches[0].set_color('lightpink')
    patches[0].set_alpha(0.6)
    patches[1].set_color('lightsteelblue')
    patches[1].set_alpha(0.6)

with open('suicide_rate_continent_title.csv', 'r', encoding = 'utf-8-sig') as f:
    df = pd.read_csv(f)
    y = df['WHO region']
    x = [2000, 2005, 2010, 2015, 2016]
    print_line(df, x, y, 0, 'Both sexes')
    print_line(df, x, y, 1, 'Male')
    print_line(df, x, y, 2, 'Female')    

with open('governance.csv', 'r', encoding = 'utf-8-sig') as f:
    df = pd.read_csv(f)
    y = df['Stand-alone mental health legislation']
    y1 = df['Mental health plan']
    y2 = df['Mental health policy']
    y3 = []
    for i in range(1, len(y)):
        if(y[i] == 'Yes' and y1[i] == 'Yes' and y2[i] == 'Yes'):
            y3 += ['Yes']
        else:
            y3 += ['No']
    the_grid = GridSpec(2, 2)
    plt.subplot(the_grid[0, 0], aspect = 1)
    print_pie(y)
    plt.title('Stand-alone mental health legislation')
    plt.subplot(the_grid[0, 1], aspect = 1)
    print_pie(y1)
    plt.title('Mental health plan')
    plt.subplot(the_grid[1, 0], aspect = 1)
    print_pie(y2)
    plt.title('Mental health policy')
    plt.subplot(the_grid[1, 1], aspect = 1)
    print_pie(y3)
    plt.title('All above')
    plt.show()

with open('taiwan_suiciderate_age.csv', 'r', encoding = 'utf-8-sig') as f:
    df = pd.read_csv(f)
    print_line_02(df)

with open('taiwan_suiciderate.csv', 'r', encoding = 'utf-8-sig') as f:
    df1 = pd.read_csv(f)
    with open('unemployment.csv', 'r', encoding = 'utf-8-sig') as g:
        df2 = pd.read_csv(g)
        x1 = df1['Year']
        x2 = df2['Year']
        y1 = df2['Total']
        y_suicide_s = df1['Suicide rate, standarized']
        y_suicide_c = df1['Suicide rate, crude']
        y_total = []
        for i in range(len(x1)):
            for j in range(len(x2)):
                try:
                    if int(x1[i]) == (int(x2[j]) - 1911):
                        y_total.append(y1[j])
                        break
                except Exception:
                    continue
        fig, ax1 = plt.subplots()
        ax1.plot(x1, y_suicide_c, color = 'darkorchid', linewidth = 2.0, linestyle = '-', label = 'Suicide rate, standarized')
        ax1.plot(x1, y_suicide_s, color = 'orchid', linewidth = 2.0, linestyle = '-', label = 'Suicide rate, crude')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Suicide rate(per 100 000 population)', color = 'darkorchid')
        ax1.tick_params('y', colors = 'darkorchid')
        leg = plt.legend(loc='upper left', ncol=1, mode="", shadow=False, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        ax2 = ax1.twinx()
        ax2.plot(x1, y_total, color = 'lightgray', linewidth = 2.0, linestyle = '--', label = 'Unemployment rate')
        ax2.set_ylabel('Unemployment rate(%)', color = 'gray')
        ax2.tick_params('y', colors = 'gray')
        leg = plt.legend(loc='upper right', ncol=1, mode="", shadow=False, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        plt.title('Suicide rate\nvs\nUnemployment rate')
        plt.show()
        se = pd.Series(y_total)
        df1['unemployment rate'] = se.values
        print(df1['Suicide rate, standarized'].corr(df1['unemployment rate']))

with open('taiwan_suiciderate_age.csv', 'r', encoding = 'utf-8-sig') as f:
    df1 = pd.read_csv(f)
    with open('unemployment.csv', 'r', encoding = 'utf-8-sig') as g:
        df2 = pd.read_csv(g)
        x1 = df1['Year']
        x2 = df2['Year']
        y1 = df2['Total']
        y_2544 = df1['25-44']
        y_4564 = df1['45-64']
        y_total = []
        for i in range(len(x1)):
            for j in range(len(x2)):
                try:
                    if int(x1[i]) == (int(x2[j]) - 1911):
                        #print(y1[j])
                        y_total.append(y1[j])
                        break
                except Exception:
                    continue
        fig, ax1 = plt.subplots()
        ax1.plot(x1, y_2544, color = 'orchid', linewidth = 2.0, linestyle = '-', label = 'Suicide rate, 25-44')
        ax1.plot(x1, y_4564, color = 'darkorchid', linewidth = 2.0, linestyle = '-', label = 'Suicide rate, 45-64')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Suicide rate(per 100 000 population)', color = 'darkorchid')
        ax1.tick_params('y', colors = 'darkorchid')
        leg = plt.legend(loc='upper left', ncol=1, mode="", shadow=False, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        ax2 = ax1.twinx()
        ax2.plot(x1, y_total, color = 'lightgray', linewidth = 2.0, linestyle = '--', label = 'Unemployment rate')
        ax2.set_ylabel('Unemployment rate(%)', color = 'gray')
        ax2.tick_params('y', colors = 'gray')
        leg = plt.legend(loc='upper right', ncol=1, mode="", shadow=False, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        plt.title('Suicide rate\nvs\nUnemployment rate')
        plt.show()
        se = pd.Series(y_total)
        df1['unemployment rate'] = se.values
        print(df1['25-44'].corr(df1['unemployment rate']))
        print(df1['45-64'].corr(df1['unemployment rate']))
    
