import pandas as pd

class ReadFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        df = pd.read_csv(self.filename)
        df.to_parquet(self.filename.replace('.csv', '.parquet'))

        return df.columns 

    def average(self, column_name):
        df = pd.read_csv(self.filename)
       
        avg_value = df[column_name].mean()
        print("Average of ", column_name, ": ",avg_value)
    
    def maximum(self, column_name):
        df = pd.read_csv(self.filename)
        
        max_value = df[column_name].max()
        print("Maximum of ", column_name, ": ",max_value)
    
    def minimum(self, column_name):
        df = pd.read_csv(self.filename)
        
        min_value = df[column_name].min()
        print("Minimum of ", column_name, ": ",min_value)

    def absolute(self, column_name):
        df = pd.read_csv(self.filename)
        
        absolute_value = df[column_name].abs()
        print("Minimum of ", column_name, ": ",absolute_value)

def main():
    filename = "iris.csv"
    file_reader = ReadFile(filename)
    file_reader.read()
    print("Average of each column: ")
    for column in file_reader.read():
        file_reader.average(column)
    print("")

    print("Maximum of each coulmn:")
    for column in file_reader.read():
        file_reader.maximum(column)
    print("")

    print("Minimum of each coulmn:")
    for column in file_reader.read():
        file_reader.minimum(column)
    print("")

    print("Absolute of each coulmn:")
    for column in file_reader.read():
        file_reader.absolute(column)
    print("")


if __name__ == "__main__":
   main()