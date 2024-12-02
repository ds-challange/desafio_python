import csv
from src.modules.airline.contracts.implementations.beanie.document import AirlineDocument

async def document_db_insert_from_csv(file_path: str, chunk_size=10000):
    """Process a CSV file and insert data into the database in batches.

    Args:
        file_path (str): Path to the CSV file.
        chunk_size (int, optional): Size of each batch for database insertion. Defaults to 100.

    Yields:
        None: Inserts data into the database in batches.
    """
    print(f"Parsing CSV file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            batch = []
            for row in reader:
                data = {key: value if value else None for key, value in row.items()}
                try:
                    document = AirlineDocument(**data)
                except Exception as e:
                    print(f"Error creating document: {e}. Data: {data}")
                    continue
                
                batch.append(document)
                if len(batch) == chunk_size:
                    try:
                        await AirlineDocument.insert_many(batch)
                        print(f"Inserted a batch of {len(batch)} documents.")
                    except Exception as e:
                        print(f"Error inserting batch: {e}")
                    batch = []
            
            if batch:
                try:
                    await AirlineDocument.insert_many(batch)
                    print(f"Inserted the last batch of {len(batch)} documents.")
                except Exception as e:
                    print(f"Error inserting final batch: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Unexpected error: {e}")
