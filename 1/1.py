calibrations = []
with open("input.txt") as input:
    lines = input.read().splitlines()
    
    for line in lines:
        first = None
        last = None 
        spelled = []
        
        # first and last index of spelled digits, -1 if not found
        spelled.append((line.find('zero'), line.rfind('zero')))
        spelled.append((line.find('one'), line.rfind('one')))
        spelled.append((line.find('two'), line.rfind('two')))
        spelled.append((line.find('three'), line.rfind('three')))
        spelled.append((line.find('four'), line.rfind('four')))
        spelled.append((line.find('five'), line.rfind('five')))
        spelled.append((line.find('six'), line.rfind('six')))
        spelled.append((line.find('seven'), line.rfind('seven')))
        spelled.append((line.find('eight'), line.rfind('eight')))
        spelled.append((line.find('nine'), line.rfind('nine')))

        for c in line:
            if '0' <= c <= '9':
                first = c
                break
        for i in range(len(line)-1, -1, -1):
            if '0' <= line[i] <= '9':
                last = line[i]
                break
        
        for i in range(len(spelled)):
            if 0 <= spelled[i][0] < line.find(first):
                first = str(i)
                break
        for i in range(len(spelled)):
            if spelled[i][1] > line.rfind(last):
                last = str(i)
                break

        # print(line.rjust(60) + ' : ' + first + last)
        calibrations.append(int(first + last))

print(sum(calibrations))




    

