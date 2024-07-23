from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")
    party3 = Party(name="Eve")

    # Inputs from parties
    x = SecretInteger(Input(name="X", party=party1))
    y = SecretInteger(Input(name="Y", party=party2))

    # Perform computations using Nada's secure operations
    result1 = x + x  # Multiply x by 2 securely
    result2 = y + y + y  # Multiply y by 3 securely

    # Combine results securely
    final_result = result1 - result2  # Perform secure subtraction

    # Output the final result securely to a third party
    return [Output(final_result, "FinalResult", party=party3)]
