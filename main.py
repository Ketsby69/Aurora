import os
import pickle

from configurations import PATH_MEMORY


if __name__ == '__main__':

    if not os.path.exists(PATH_MEMORY):

        with open(PATH_MEMORY, "wb") as f:

            pickle.dump({}, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    from sensory_neuron import EncoderCharacteristics

    interaction = input("interaction: ")

    data = EncoderCharacteristics(characters=interaction).encoder_characteristics()

    print(data)