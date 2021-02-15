from dwave.system import DWaveSampler
sampler_manual = DWaveSampler(solver={'topology__type': 'chimera'})

all(qubit in sampler_manual.nodelist for qubit in [0, 1, 4, 5])   
all(coupler in sampler_manual.edgelist for coupler in [(0, 4), (0, 5), (1, 4), (1, 5)])

qubit_biases = {(0, 0): 1, (1, 1): -1, (4, 4): -1, (5, 5): 1}
coupler_strengths = {(0, 4): 2, (0, 5): -3, (1, 4): 2, (1, 5): 2}
Q = {**qubit_biases, **coupler_strengths}

sampleset = sampler_manual.sample_qubo(Q, num_reads=5000)

print(sampleset)
