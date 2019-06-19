import time

def nwd(x,y):
    while x != y:
        if x > y:
            x -= y
        elif x < y:
            y -= x
    return x

if __name__ == '__main__':
    t1 = time.time()

    output = open('wynik.txt', 'a')

    with open("liczby.txt") as file:
        file = file.readlines()
        result = {'nwd': 0, 'rows': 0, 'row_start': 0}
        current = {'nwd': 0, 'rows': 0, 'row_start': 0}

        for x, y in zip(file[1:], file[2:]):
            nwdd = nwd(int(x),int(y))
            if nwdd == 1:
                if current['rows'] > result['rows']:
                    result['nwd'] = current['nwd']
                    result['rows'] = current['rows']
                    result['row_start'] = current['row_start']
                current['nwd'] = 0
                current['rows'] = 0
                current['row_start'] = 0
            else:
                if nwdd == current['nwd']:
                    current['rows'] += 1
                else:
                    if current['rows'] > result['rows']:
                        result['nwd'] = current['nwd']
                        result['rows'] = current['rows']
                        result['row_start'] = current['row_start']
                    current['nwd'] = nwdd
                    current['rows'] = 1
                    current['row_start'] = x

    output.write(str(result['row_start'])+ " "+str(result['rows']+2)+ " " + str(result['nwd']))
    output.close()

print(time.time() - t1)
