import numpy as np
from skribbl.neuron import Neuron # Adjust the import based on your file structure

def test_neuron_forward():
    # Test case 1: Known weights and bias
    num_inputs = 3
    neuron = Neuron(num_inputs)
    neuron.weights = np.array([0.5, -0.2, 0.1])
    neuron.bias = 0.4
    inputs = np.array([1.0, 2.0, 3.0])
    expected_output = np.dot(neuron.weights, inputs) + neuron.bias
    output = neuron.forward(inputs)
    assert np.isclose(output, expected_output), f"Expected {expected_output}, but got {output}"
    
    # Test case 2: Zero weights and bias
    neuron.weights = np.zeros(num_inputs)
    neuron.bias = 0.0
    inputs = np.array([1.0, 2.0, 3.0])
    expected_output = 0.0
    output = neuron.forward(inputs)
    assert np.isclose(output, expected_output), f"Expected {expected_output}, but got {output}"

    # Test case 3: Random weights and bias
    neuron.weights = np.random.randn(num_inputs)
    neuron.bias = np.random.randn()
    inputs = np.random.randn(num_inputs)
    expected_output = np.dot(neuron.weights, inputs) + neuron.bias
    output = neuron.forward(inputs)
    assert np.isclose(output, expected_output), f"Expected {expected_output}, but got {output}"

if __name__ == "__main__":
    test_neuron_forward()
    print("All tests passed!")