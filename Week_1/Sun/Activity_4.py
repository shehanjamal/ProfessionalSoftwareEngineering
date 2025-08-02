import numpy as np

def display_rainfall_numpy():
    rainfall_= [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    print(np.array(rainfall_))

def display_rainfall_total():
    rainfall_= np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    print("Total rainfall: ",np.sum(rainfall_))

def display_rainfall_average():
    rainfall_= np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    print("Average rainfall: ",np.average(rainfall_))

def display_rainfall_count_greater_than_20():
    rainfall_= np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    count_ = 0
    for i in rainfall_:
        if i > 20:
            count_ += 1
    print("Rainfall greater than 20: ", count_)

def display_rainfall_count_greater_than_5():
    rainfall_ = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    index_ = np.where(rainfall_ > 5)

    print("Rainfall greater than 5: ", rainfall_[index_])
    print("Rainfall index greater than 5: ", index_)


if __name__ == "__main__":
    display_rainfall_numpy()
    display_rainfall_total()
    display_rainfall_average()
    display_rainfall_count_greater_than_20()
    display_rainfall_count_greater_than_5()