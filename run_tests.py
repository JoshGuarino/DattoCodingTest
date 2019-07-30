from simulation_files import sim, special_case

def test(gw, rp, off):
    test_data = []
    print('\nrunning test...')
    for i in range(10):
        test_data.append(round(sim.run_test(gw, rp, off), 2))
        print('Run ' + str(i+1) +': ' + str(test_data[i]) + ' mins')
    avg = round(sum(test_data)/len(test_data), 2)
    print('Average total upgrade time: ' + str(avg) + ' mins')

def spec_case(gw, rp, off):
    print('\nrunning special case...')
    test_data = [[0,0],[0,0],[0,0],[0,0]]
    for i in range(10):
        test = special_case.run_test(gw, rp, off)
        print('\nRun ' + str(i+1) + ':')
        print('Not started: ' + str(test[0][0]) + ' Gateways and ' + str(test[0][1]) + ' Repeaters')
        print('Downloading: ' + str(test[1][0]) + ' Gateways and ' + str(test[1][1]) + ' Repeaters')
        print('Upgrading: ' + str(test[2][0]) + ' Gateways and ' + str(test[2][1]) + ' Repeaters')
        print('Complete: ' + str(test[3][0]) + ' Gateways and ' + str(test[3][1]) + ' Repeaters')
        test_data[0][0] = test_data[0][0] + test[0][0]
        test_data[0][1] = test_data[0][1] + test[0][1]
        test_data[1][0] = test_data[1][0] + test[1][0]
        test_data[1][1] = test_data[1][1] + test[1][1]
        test_data[2][0] = test_data[2][0] + test[2][0]
        test_data[2][1] = test_data[2][1] + test[2][1]
        test_data[3][0] = test_data[3][0] + test[3][0]
        test_data[3][1] = test_data[3][1] + test[3][1]
    print('\nTotal over 10 runs:')
    print('Not started: ' + str(test_data[0][0]) + ' Gateways and ' + str(test_data[0][1]) + ' Repeaters')
    print('Downloading: ' + str(test_data[1][0]) + ' Gateways and ' + str(test_data[1][1]) + ' Repeaters')
    print('Upgrading: ' + str(test_data[2][0]) + ' Gateways and ' + str(test_data[2][1]) + ' Repeaters')
    print('Complete: ' + str(test_data[3][0]) + ' Gateways and ' + str(test_data[3][1]) + ' Repeaters')

if __name__ == "__main__":
    test(10, 2, 5)
    spec_case(10, 2, 5)
    test(3, 4, 5)
    test(4, 3, 5)
    test(10, 2, 6)