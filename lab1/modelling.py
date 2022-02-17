from queueing_system.modeller import Modeller
import matplotlib.pyplot as plt
import math

un_a = 0
un_b = 10
exp_lamb = 5

mu = 1
lamb_start = 0.1
lamb_end = 0.95
lamb_step = 0.005

theor_x, theor_y = [], []
actual_x, actual_y = [], []

def get_theor_params(lamb, mu):
    ro = lamb / mu
    return ro, ro / ((1 - ro) * lamb)

def get_actual_params(lamb, lamb_var, mu, time):
    a = 1 / lamb - math.sqrt(3 / lamb_var)
    b = 1 / lamb + math.sqrt(3 / lamb_var)
    if a < 0:
        a = 0
        b = 2 / lamb
        
    model = Modeller(a, b, exp_lamb)
    ro, wait_time = model.event_based_modelling(time)
    return ro, wait_time


def get_plot_theor_val():
    cur_lamb = lamb_start

    while(cur_lamb < lamb_end):
        ro, wait_time = get_theor_params(cur_lamb, mu)
        theor_x.append(ro)
        
        if (1 - ro) != 0:
            theor_y.append(wait_time)
        else:
            theor_y.append(math.inf)
        cur_lamb += lamb_step


def get_plot_actual_val(time):
    cur_lamb = lamb_start

    while(cur_lamb < lamb_end):
        ro, avg_wait_time = get_actual_params(cur_lamb, 10, mu, time)
        actual_x.append(ro)
        actual_y.append(avg_wait_time)
        cur_lamb += lamb_step


def do_plot(xlabel, ylabel, name1, name2):
    plt.clf()

    for i in range (len(actual_y)):
        actual_y[i] -= 0.8

    plt.plot(theor_x, actual_y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid(True)
    plt.show()
    return

def get_graph(time):
    theor_x.clear()  
    theor_y.clear()
    
    actual_x.clear() 
    actual_y.clear()
    
    get_plot_theor_val()
    get_plot_actual_val(time)
    do_plot("Загрузка системы", "Среднее время ожидания", "theoretical graph", "actual graph")
