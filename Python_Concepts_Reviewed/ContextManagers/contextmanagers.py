"""
Create a custom context manager class named LoggedFile that:

✅ Requirements:
	•	Accepts file path and mode ('r', 'w' etc.) during initialization.
	•	When entering (__enter__):
	•	Opens the file.
	•	Prints:
👉 "[OPEN] File <filename> opened in <mode> mode"
	•	When exiting (__exit__):
	•	Automatically closes the file, even if an exception occurred.
	•	Prints:
👉 "[CLOSE] File <filename> closed"
	•	If any exception occurs inside the context, log:
👉 "[ERROR] <ExceptionType>: <message>"
and suppress it (return True) ONLY if it’s FileNotFoundError. Otherwise let it propagate.

If FileNotFoundError happens → it should be suppressed.
If another exception like ValueError happens → it should be raised after cleanup.

⸻

Usage - 
with LoggedFile("test.txt", "w") as f:
    f.write("Hello!")
    # Manually raise some test exception to see exit behavior



🚀 Bonus (Optional – for Senior Level)

Add timing:
	•	Record time in __enter__
	•	On __exit__, print:
👉 "Execution time inside context: X.XXX seconds"
"""
import time

class LoggedFile:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.f = None
        self.file_name = None
        self.start = None
        self.end = None

    def __enter__(self):
        self.file_name = self.file_path.split("/")[-1]
        self.start = time.time()
        self.f = open(self.file_path, encoding="utf-8", mode=self.mode)
        print(f'[OPEN] File {self.file_name} opened in {self.mode} mode')
        return self.f

    def __exit__(self, exc_type, exc, tb):
        try:
            if self.f and not self.f.closed:
                self.f.close()
        finally:
            print(f'[CLOSE] File {self.file_name} closed')
            self.end = time.time()
            print(f"Execution time inside context: {self.end - self.start} seconds")
        if exc_type is not None:
            print(f'[ERROR] {exc_type.__name__}: {str(exc)}')
            return issubclass(exc_type, FileNotFoundError)
        return False

if __name__ == '__main__':
    file_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Python_Concepts_Reviewed/ContextManagers/test.txt"
    with LoggedFile(file_path, 'w') as f:
        f.write('Arjun Shome')
    

