import pickle
from dataclasses import dataclass
import os

from configurations import PATH_MEMORY

assignment_dict : dict = pickle.load(open(PATH_MEMORY, "rb"))

@dataclass
class EncoderCharacteristics:

    characters: str

    def __verify_characteristics(self) -> None:

        assignment_dict_number: int = len(assignment_dict)
        list_characters: list = list(self.characters)
        assignment_number: int = assignment_dict_number

        for character in list_characters:

            if character not in assignment_dict:
                assignment_number += 1
                assignment_dict[character] =  assignment_number
        
        if assignment_dict_number != assignment_number:
            with open(PATH_MEMORY, "wb") as f:
                pickle.dump(assignment_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

        print(assignment_dict)

    def encoder_characteristics(self) -> list[list[int]]:

        self.__verify_characteristics()

        concepts: list = self.characters.split()

        vector_concepts: list = list()

        for x in concepts:

            vector_concept: list = list()

            for y in x:

                vector_concept.append(assignment_dict[y])

            vector_concepts.append(vector_concept)

        return vector_concepts
