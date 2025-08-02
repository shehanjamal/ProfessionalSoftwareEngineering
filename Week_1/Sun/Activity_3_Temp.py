import numpy as np

def avg_temp():
    z = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    return np.mean(z)

def highest_lowest_temp():
    z = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    print("Highest Temperature is:",np.max(z))
    print("Lowest Temperature is:",np.min(z))

def convert_to_fahrenheit():
    z = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    return z * 9/5 + 32

def temp_exceed_20():
    z = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    for i in z:
        if i>=20:
            print("Temperature " ,i," exceeds 20.")
    exc = z >= 20
    print("Temperatures exceeding 20:", z[exc])
    print("All Temperatures:", z)

def temp_exceed_20_SOULUTION():
    z = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    temp = np.where (z > 20)
    print("Temperatures exceeding 20 (0=MON, 7=SUN):", z[temp])
    print("All Temperatures:", z)


    
    

if __name__ == "__main__":
    ans = avg_temp()
    print("Mean Temp is:", ans)
    highest_lowest_temp()
    print("Temperatures in Fahrenheit:", convert_to_fahrenheit())
    print("My solution")
    temp_exceed_20()
    print("Soulution Shown")
    temp_exceed_20_SOULUTION()