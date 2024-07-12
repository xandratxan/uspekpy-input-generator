from generator import generate_input_file

# Input file 1: Input file for Hp(10, slab) and low N qualities
# Define input file parameters
cases = [
    ('N10', 'Hp(10, slab)'),
    ('N20', 'Hp(10, slab)'),
    ('N30', 'Hp(10, slab)')
]
air_gap = 1000  # mm
anode_angle = 20  # deg
iterations = 500
mu_tr_rho_file_path = 'my_mu_tr_rho_file'
h_k_file_path = 'my_h_k_file'
output_path = 'my_input'

# Run input file generator
generate_input_file(cases, iterations, air_gap, anode_angle, mu_tr_rho_file_path, h_k_file_path, output_path)
