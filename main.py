import os
import pickle
from encoders import EncoderCharacteristics




if __name__ == '__main__':

    path_base = os.path.dirname(__file__)
    path_database = path_base + "/database/database_encoder_characteristics.pkl"

    if not os.path.exists(path_database):

        with open(path_database, "wb") as f:

            pickle.dump({}, f, protocol=pickle.HIGHEST_PROTOCOL)

    interaction = input("interaction: ")

    EncoderCharacteristics(path=path_database,characters=interaction).verify_characteristics()