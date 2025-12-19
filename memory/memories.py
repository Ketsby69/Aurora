import pickle
from dataclasses import dataclass, field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_MEMORY = BASE_DIR / "memory"

@dataclass
class Memory:

    name_file :str
    path: Path = field(init=False)

    def __post_init__(self):
        self.path = PATH_MEMORY / self.name_file
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def create_memory(self) -> None:
        self.save_memory({})

    def load_memory(self) -> dict[any, any]:

        if not self.verify_file():
            self.create_memory()

        try:
            with open(self.path, 'rb') as memory_file:
                return pickle.load(memory_file)
        except (EOFError, pickle.UnpicklingError):
            self.create_memory()
            with open(self.path, 'rb') as memory_file:
                return pickle.load(memory_file)

    def save_memory(self, dict_memory: dict[any, any]) -> None:

        with open(self.path, 'wb') as memory_file:
            pickle.dump(dict_memory, memory_file)

    def verify_file(self) -> bool:
        return Path(self.path).is_file()