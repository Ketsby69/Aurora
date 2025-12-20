from dataclasses import dataclass, field
from memory import Memory

MEMORY_NAME = "memory_characterics.pkl"


@dataclass
class EncoderTextCharacteristics:

    characters: str
    memory: Memory = field(default_factory=lambda: Memory(MEMORY_NAME))
    dict_memory: dict[str, int] = field(init=False)

    def __post_init__(self):
        self.dict_memory = self.memory.load_memory()

    def __verify_characteristics(self) -> None:

        next_number = len(self.dict_memory) + 1
        updated = False

        for char in self.characters:
            if char not in self.dict_memory:
                self.dict_memory[char] = next_number
                next_number += 1
                updated = True

        if updated:
            self.memory.save_memory(self.dict_memory)

    def encoder_characteristics(self) -> list[int]:

        self.__verify_characteristics()

        vector_concepts = []

        for word in self.characters.split():

            encoded_word = int(''.join(str(self.dict_memory[char]) for char in word))
            vector_concepts.append(encoded_word)

        return vector_concepts