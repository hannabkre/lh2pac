from gemseo.core.discipline import MDODiscipline
from gemseo.utils.data_conversion import concatenate_dict_of_arrays_to_array
from gemseo.utils.data_conversion import split_array_to_dict_of_arrays


class MyMLAlgo(MDODiscipline):
    """foo."""

    def __init__(self, algo, input_names, output_names):
        self.algo = algo
        super().__init__()
        self.input_grammar.update_from_names(input_names)
        self.output_grammar.update_from_names(output_names)

    def _run(self) -> None:
        input_data = self.get_input_data()
        input_vector = concatenate_dict_of_arrays_to_array(
            input_data, self.input_grammar.names
        )
        output_vector = self.algo.predict(input_vector)
        output_data = split_array_to_dict_of_arrays(
            output_vector, dict.fromkeys(self.output_grammar.names, 1)
        )
        self.store_local_data(**output_data)
