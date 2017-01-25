with open('out.txt') as f:
    for line in f:
        features_, classes = line.strip().split(None, 1)
        y = classes.split(',')
        features = features_.split(',')[1:]
        if len(features) > 1000:
            print('NEWLINE', line.strip())