from sensory_neuron import SensoryNeurons


if __name__ == '__main__':

    interaction = input("interaction: ")

    data = SensoryNeurons(stimulus=interaction).create_sensory_neurons()

    print(data)