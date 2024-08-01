import csv

def add_to_csv(model, convertbot_count, filename='output.csv'):
    """
    Appends a new row with the model and convertbot_count to the specified CSV file.
    
    Args:
        model (str): The model name or identifier to be added to the CSV.
        convertbot_count (int): The count associated with the model to be added to the CSV.
        filename (str): The name of the CSV file (default is 'output.csv').
    """

    # Open the CSV file in append mode ('a')
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the new row
        writer.writerow([model, convertbot_count])

# Example usage
add_to_csv('ModelX', 42)
add_to_csv('ModelY', 15)
