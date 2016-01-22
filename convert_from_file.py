"""Open and read in data from a .txt file. Each line of the file is in
the format:
<positive_integer>,<string>
If the positive integer is odd, write the string out to a new file in
all capital letters. If the positive integer is even, write the string
out to the new file as it appears.
"""
import convert_odd_input

def read_file(file_name):
    """Read in data from a file and return it."""
    some_file = open(file_name, 'r')
    data = some_file.read()
    file.close()
    return data

def write_file(info):
    """Take a string called 'info' and break it into chunks in the
    format:
    <positive_integer>,<string>
    Then convert each chunk and write the conversion out to a new file
    called output.txt.
	"""
    new_file = open('output.txt', 'w')
    chunks = info.splitlines()
    for chunk in chunks:
        new_file.write(convert_odd_input.convert(chunk)+'\n')
    new_file.close()

if __name__ == "__main__":
    DATA = read_file('convert_this_data.txt')
    write_file(DATA)
