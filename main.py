import os
import pickle

from configurations import PATH_MEMORY


if __name__ == '__main__':

    if not os.path.exists(PATH_MEMORY):

        with open(PATH_MEMORY, "wb") as f:

            pickle.dump({}, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    from sensory_neuron import EncoderTextCharacteristics

    interaction = input("interaction: ")

    data = EncoderTextCharacteristics(characters=interaction).encoder_characteristics()

    print(data)