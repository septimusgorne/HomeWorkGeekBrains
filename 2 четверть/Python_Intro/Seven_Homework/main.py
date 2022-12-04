import user_reader
import file_reader
import file_writer

flag, data = user_reader.initial()
if flag == 'search':
    file_reader.read_data(data)
else:   
    file_writer.write(flag, data)