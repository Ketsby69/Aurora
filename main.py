from sensory_neuron import EncoderTextCharacteristics


if __name__ == '__main__':

    interaction = input("interaction: ")

    data = EncoderTextCharacteristics(characters=interaction).encoder_characteristics()

    print(data)