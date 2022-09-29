def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    #raise NotImplementedError()
    
    from csv import reader
    
    with open('students.csv', 'r') as file:
        csv_reader = reader(file)
    
    return (list(csv_reader))

