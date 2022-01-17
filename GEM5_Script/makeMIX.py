#!/bin/python3
from itertools import combinations

benchName = {
    'mcf' : 'inp.in',
    'lbm' : '3000 reference.dat 0 0 100_100_130_ldc.of',
    'milc' : '<su3imp.in',
    'sphinx3' : './ctlfile . args.an4',
    'GemsFDTD' : '',
    'leslie3d' : '<leslie3d.in',
    'cactusADM' : 'benchADM.par',
    'bzip2' : 'chicken.jpg 30',
    'h264ref' : '-d foreman_ref_encoder_baseline.cfg',
    'astar' : 'rivers.cfg',
    'libquantum' : '1397 8',
    #'povray' : 'SPEC-benchmark-ref.ini'
    #'gcc' : '166.i -o 166.s',

    #'soplex' : '-s1 -e -m45000 pds-50.mps',
    #'omnetpp' : 'omnetpp.ini',

    #'bwaves' : 'bwaves.in',
    #'zeusmp' : '',
    #'xalancbmk' : '-v t5.xml xalanc.xsl',
}

benchName_keys = list(benchName.keys())

bench = list(combinations(benchName_keys, 4))




'''
for name1 in benchName_keys :
    for name2 in benchName_keys[benchName_keys.index(name1) + 1:] :
        for name3 in benchName_keys[benchName_keys.index(name2) + 1:] :
            for name4 in benchName_keys[benchName_keys.index(name3) + 1:] :
                temp_list = [name1, name2, name3, name4]
                #temp_list.sort()
                temp_set = set(temp_list)
                print(temp_list)
'''

for temp in range(0,len(bench)) :
    print('mix;' + bench[temp][0] + ';' + bench[temp][1] + ';' + bench[temp][2] + ';' + bench[temp][3] + ' : ',end = '')
    print(benchName[bench[temp][0]] + ';' + benchName[bench[temp][1]] + ';' +benchName[bench[temp][2]] + ';' +benchName[bench[temp][3]])


print(len(bench))
