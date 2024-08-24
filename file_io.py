import io
# import os

# print(os.getcwd())

payload_path = r'E:\Test Projects\task2.csv'
write_file_path = r'E:\Test Projects\sample.csv'

with open(payload_path, "r", encoding="utf-8") as payload:
    read_file = io.StringIO(payload.read())
read_file.seek(0)

with open(write_file_path, "w", encoding="utf-8") as write_file:
    read_content = read_file.read()
    write_file.write(read_content)
    if write_file.write(read_content):
        print("File written successfully")
    else:
        print("File write failed")
read_file.seek(0)

read_file.close()
