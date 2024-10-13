def solve(path):
    line_counter = 0
    # comment_counter = 0
    with open(path, 'r') as f:
        while(True):
            line = f.readline()
            if line == '':
                break
            if len(line.strip()) != 0:
                if line.strip()[0] == "#":
                    continue
                else:
                    line_counter += 1
            elif len(line.strip()) == 0:
                continue
                
    return(line_counter)
        
