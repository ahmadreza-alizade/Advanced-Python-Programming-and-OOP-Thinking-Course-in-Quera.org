def csv_reader(path):
    with open(path, 'r') as file:
        for row in file.readlines():
            yield list(map(int, row.rstrip().split(",")))


def csv_writer(path, lines, sum_row):
    with open(path, 'w') as ans:
      counter = 0
      for s in sum_row:
        ans.write(lines[counter].strip() + ", " + str(s) + "\n")
        counter += 1

def process(path):
    sum_row = list()
    for row in csv_reader(path):
        sum_row.append(sum(row))
    
    with open(path, 'r') as file_lines:
      lines = file_lines.readlines()
      
    csv_writer('ans.csv', lines, sum_row)

    pass
ستون CSV
