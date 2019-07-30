import sim
import special_case

def test(gw, rp, off):
    test_data = []
    print('\nrunning test...')
    for i in range(10):
        test_data.append(round(sim.run_test(gw, rp, off), 2))
        print('Run ' + str(i+1) +': ' + str(test_data[i]) + ' mins')
    avg = round(sum(test_data)/len(test_data), 2)
    print('Average total upgrade time: ' + str(avg) + ' mins')

def run_spec_case():
    print('\nrunning special case...')

if __name__ == "__main__":
    test(10, 2, 5)
    test(3, 4, 5)
    test(4, 3, 5)
    test(10, 2, 6)