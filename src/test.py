import os
import subprocess
import pickle


def unsafe_deserialization(data):
    return pickle.loads(data)


def command_injection(user_input):
    os.system("echo " + user_input)


def sql_injection(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    # Execute query (simulated)
    print(f"Executing query: {query}")


def main():
    # Unsafe deserialization
    serialized_data = pickle.dumps({"key": "value"})
    unsafe_deserialization(serialized_data)

    # Command injection
    user_input = input("Enter a filename to echo: ")
    command_injection(user_input)

    # SQL injection
    user_id = input("Enter user ID: ")
    sql_injection(user_id)


if __name__ == "__main__":
    main()
