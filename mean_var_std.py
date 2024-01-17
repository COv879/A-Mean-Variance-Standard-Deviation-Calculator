import numpy as np
np.set_printoptions(floatmode='maxprec', precision=15, suppress=False)



def calculate(list):
    size = 9

    if len(list) != size:
        raise ValueError("List must contain nine numbers.")


    list_array = np.array(list)
    matrix = list_array.reshape(3,3)

    def Mean(matrix):
        return np.mean(matrix)

    def Mean_Rows (matrix):
        mean_rows = np.mean(matrix, axis=0)
        mean_rows = mean_rows.tolist()
        return mean_rows
    
    def Mean_Columns(matrix):
        mean_columns = np.mean(matrix, axis=1)
        mean_columns = mean_columns.tolist()
        return mean_columns

    def Var(matrix):
        return np.var(matrix)
    
    def Var_Rows(matrix):
        var_rows = np.var(matrix, axis=0)
        var_rows = var_rows.tolist()
        return var_rows
    
    def Var_Columns(matrix):
        var_columns = np.var(matrix, axis=1)
        var_columns = var_columns.tolist()
        return var_columns

    def Std(matrix):
        return np.std(matrix).tolist()
    
    def Std_Rows(matrix):
        std_rows = np.std(matrix, axis=0)
        std_rows = std_rows.tolist()
        return std_rows
        
    
    def Std_Columns(matrix):
        std_columns = np.std(matrix, axis=1)
        std_columns = std_columns.tolist()
        return std_columns
    
    def Max_Rows(matrix):
        max_rows = np.max(matrix, axis=0)
        max_rows = max_rows.tolist()
        return max_rows
    
    def Max_Columns(matrix):
        max_columns = np.max(matrix, axis=1)
        max_columns = max_columns.tolist()
        return max_columns
    
    def Min_Rows(matrix):
        min_rows = np.min(matrix, axis=0)
        min_rows = min_rows.tolist()
        return min_rows
    
    def Min_Columns(matrix):
        min_columns = np.min(matrix, axis=1)
        min_columns = min_columns.tolist()
        return min_columns
    
    def Sum_Rows(matrix):
        sum_rows = np.sum(matrix, axis=0)
        sum_rows = sum_rows.tolist()
        return sum_rows
    
    def Sum_Columns(matrix):
        sum_columns = np.sum(matrix, axis=1)
        sum_columns = sum_columns.tolist()
        return sum_columns
        

    calculations = {
        'mean': [Mean_Rows(matrix),Mean_Columns(matrix), Mean(matrix)],
        'variance': [Var_Rows(matrix), Var_Columns(matrix), Var(matrix)],
        'standard deviation': [Std_Rows(matrix), Std_Columns(matrix), Std(matrix)],
        'max': [Max_Rows(matrix), Max_Columns(matrix), np.max(matrix)],
        'min': [Min_Rows(matrix), Min_Columns(matrix), np.min(matrix)],
        'sum': [Sum_Rows(matrix), Sum_Columns(matrix), np.sum(matrix)],
    }

    

    for calculation in calculations:
        print(f"{calculation} = {calculations[calculation]}\n")

    return calculations