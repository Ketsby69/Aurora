import pickle
from dataclasses import dataclass


@dataclass
class EncoderCharacteristics:

    path: str
    characters: str

    def verify_characteristics(self) -> None:

        assignment_dict : dict = pickle.load(open(self.path, "rb"))
        assignment_dict_number: int = len(assignment_dict)
        list_characters: list = list(self.characters)
        assignment_number: int = assignment_dict_number

        for character in list_characters:

            if character not in assignment_dict:
                assignment_number += 1
                assignment_dict[character] =  assignment_number
        
        if assignment_dict_number != assignment_number:
            with open(self.path, "wb") as f:
                pickle.dump(assignment_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

        print(assignment_dict)