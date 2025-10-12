"""
Create a class called DBConnection that ensures only one instance ever exists, no matter how many times it is instantiated.

✅ Requirements:
	1.	Implement the Singleton pattern in Pythonic way.
	2.	If someone does:
        db1 = DBConnection("db://localhost")
        db2 = DBConnection("db://remote-host")

    👉 Both db1 and db2 must be the same instance (db1 is db2 → True).
	3.	Bonus (Strong evaluation):
	•	If multiple threads try to create the object at the same time, still only one instance should exist (thread-safe Singleton).
	•	Print a log message inside __init__ only once, no matter how many times it’s called.
	•	Prevent direct instantiation via constructor abuse (like forcing new instances manually).

    🎯 Expected Usage Test
    db1 = DBConnection("localhost")
    db2 = DBConnection("remote")
    print(db1 is db2)  # Should be True
    print(db1.connection_string)  # Should still show "localhost"

    🧨 Extra Interview Twist (optional):
	•	Try to break your singleton manually and then patch the vulnerability.
    Example: using copy.copy() or pickle.

"""


class DBConnection:
    _instance = None
    _con_str = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
        if not cls._con_str:
            cls._con_str = args[0]
        return cls._instance
    
    @property
    def connection_string(self):
        return self._con_str


if __name__=='__main__':
    db1 = DBConnection("localhost:5432//api")
    db2 = DBConnection("external_srvr:3324//api")

    print(db1 is db2)
    print(db1.connection_string)