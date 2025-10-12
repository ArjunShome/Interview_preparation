"""
Write a generator function called chunked_reader(file_path, chunk_size) that:
	•	Opens a large text file lazily (without loading the whole file into memory).
	•	Reads the file line by line, but yields chunks of chunk_size lines at a time as a list.
	•	After each chunk is yielded, it should print: "Yielded chunk of {n} lines" where n is the number of lines in that chunk.
	•	The generator should automatically stop when the file ends — even if the last chunk has fewer than chunk_size lines.

Bonus Points (optional, to test deeper generator understanding)

Add a feature where sending True into the generator via send() forces it to skip the next chunk instead of yielding it.
"""

class FileReader:
    def __init__(self, file_path: str, chunksize: int):
        self.file_path = file_path
        self.chunk_size = chunksize

    def chunked_reader(self):
        list_data_lines = []
        is_end_of_file = False
        with open(self.file_path, encoding="utf-8") as f:
            while not is_end_of_file:
                i = 1
                while i <= self.chunk_size:
                    line = f.readline()
                    if line:
                        list_data_lines.append(line)
                        i += 1
                    else:
                        is_end_of_file = True
                        break
                if len(list_data_lines) > 0:
                    yield list_data_lines
                    list_data_lines = []

    def retrieve_file_data(self):
        reader = self.chunked_reader()
        for data in reader:
            print(f"Yielded Chunk of {len(data)} Lines")


def main():
    file_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Python_Concepts_Reviewed/Generators/transactions.txt"
    file_reader = FileReader(file_path, 5)
    file_reader.retrieve_file_data()


if __name__=='__main__':
    main()