from dataclasses import dataclass, field
from sensory_neuron import EncoderTextCharacteristics
from memory import Memory

MEMORY_NAME = "memory_sensory_neurons.pkl"

@dataclass
class SensoryNeurons:
    stimulus: str
    memory: Memory = field(default_factory=lambda: Memory(MEMORY_NAME))
    dict_memory: dict = field(init=False)

    def __post_init__(self):
        self.dict_memory = self.memory.load_memory()

    def __update_relations_node(self, node: int, target_nodes: list[int]):
        if node not in self.dict_memory:
            self.dict_memory[node] = {target: 1 for target in target_nodes if target != node}
        else:
            current_relations = self.dict_memory[node]
            for target in target_nodes:
                if target != node:
                    current_relations[target] = current_relations.get(target, 0) + 1

    def create_sensory_neurons(self):
        
        vector_concepts = EncoderTextCharacteristics(self.stimulus).encoder_characteristics()

        if not isinstance(vector_concepts, list):
            return self.dict_memory

        for node in vector_concepts:
            self.__update_relations_node(node, vector_concepts)

        self.memory.save_memory(self.dict_memory)

        return self.dict_memory









