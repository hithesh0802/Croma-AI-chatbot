import pandas as pd
from datasets import Dataset

def preprocess_financial_data(csv_file, output_file):
    # Load the CSV data
    data = pd.read_csv(csv_file)
    
    # Transpose the dataset so that the years become rows
    data = data.set_index('Corporate actions').transpose()
    
    # Rename the index (which now contains the years) to 'Year'
    data.index.name = 'Year'
    data.reset_index(inplace=True)
    
    # Initialize lists to store inputs and outputs
    inputs = []
    outputs = []
    
    # Iterate over the rows in the dataframe
    for _, row in data.iterrows():
        # Construct the input string from the columns
        input_text = f"Year: {row['Year']}, Equity Capital: {row['Equity Capital']}, Reserves: {row['Reserves']}, Borrowings: {row['Borrowings +']}, Other Liabilities: {row['Other Liabilities +']}, Total Liabilities: {row['Total Liabilities']}, Fixed Assets: {row['Fixed Assets +']}, CWIP: {row['CWIP']}, Investments: {row['Investments']}, Other Assets: {row['Other Assets +']}, Total Assets: {row['Total Assets']}"
        
        # Example output could be a summary or specific insight
        output_text = f"In {row['Year']}, the company had total liabilities of {row['Total Liabilities']} with reserves at {row['Reserves']} and borrowings at {row['Borrowings +']}."
        
        # Append the formatted input and output to the lists
        inputs.append(input_text)
        outputs.append(output_text)
    
    # Create a dataset from the preprocessed data
    dataset = Dataset.from_dict({'input_text': inputs, 'target_text': outputs})
    
    # Save the dataset for future use
    dataset.save_to_disk(output_file)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_financial_data("bajaj_balance_sheet.csv", "processed_dataset")
