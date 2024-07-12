import metpyx as mx
import pandas as pd


def generate_input_file(cases, iterations, air_gap, anode_angle, mu_tr_rho_file_path, h_k_file_path, output_path):
    # USpekPy batch_simulation() input file first column
    names = [
        'General',
        'Quality',
        'Operational quantity',
        'Irradiation angle (deg)',
        'Number of simulations',
        'Values',
        'Al filter width (mm)',
        'Cu filter width (mm)',
        'Sn filter width (mm)',
        'Pb filter width (mm)',
        'Be filter width (mm)',
        'Air gap width (mm)',
        'Peak kilovoltage (kV)',
        'Anode angle (deg)',
        'Mass energy transfer coefficients of air file (keV and cm²/g)',
        'Mono-energetic K to H conversion coefficients file (keV and Sv/Gy)',
        'Relative uncertainties (k=1)',
        'Al filter width (fraction of one)',
        'Cu filter width (fraction of one)',
        'Sn filter width (fraction of one)',
        'Pb filter width (fraction of one)',
        'Be filter width (fraction of one)',
        'Air gap width (fraction of one)',
        'Peak kilovoltage (fraction of one)',
        'Anode angle (fraction of one)',
        'Mass energy transfer coefficients of air (fraction of one)',
    ]
    i = 1  # Case counter
    input_headers = ['Names']  # List to store input file columns headers
    input_columns = [names]  # List to store input file columns data

    # Iterate over every case (quality, quantity)
    for quality, quantity in cases:
        # Get irradiation angles for the operational quantity
        xqt = mx.XrayQuantities()
        angles = xqt.get_irradiation_angles(quantity)

        # Iterate over every angle:
        for angle in angles:
            # Case name
            name = f'Case{i}'

            # General parameters
            general_parameters = [quality, quantity, angle, iterations]

            # Values parameters
            # Initialize XrayQualities object
            xql = mx.XrayQualities()
            # Get peak kilovoltaje for the radiation quality
            kvp = xql.get_peak_kilovoltage(quality)
            # Get filtration thicknesses for the radiation quality
            filtration_dict = xql.get_filtration_thickness(quality)
            # List filtration thicknesses ordered as in the input file
            materials = ['Al', 'Cu', 'Sn', 'Pb', 'Be']
            filtration_list = [filtration_dict[mat] for mat in materials]
            # List of values parameters
            value_parameters = filtration_list + [air_gap, kvp, anode_angle, mu_tr_rho_file_path, h_k_file_path]

            # Uncertainty parameters
            uncertainty_parameters = [0] * 9

            # Case parameters
            column = [''] + general_parameters + [''] + value_parameters + [''] + uncertainty_parameters

            # Append to cases list
            input_headers.append(name)
            input_columns.append(column)
            # Increment case counter
            i += 1

    # Build DataFrame equivalent to the input file
    df = pd.DataFrame(input_columns)
    df = df.T
    df.columns = input_headers
    print(df.to_string())
    df.to_csv(output_path, index=False)
