from chatterbot.logic import LogicAdapter
import random


class WeatherLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['weather', 'how to beat the cold',
                 'it is so cold', 'how to beat the weather', 'how to keep warm']
        if any(x in statement.text for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        # make it generate a deferent response each time.
        from chatterbot.conversation import Statement
        advices = ['stay in the upstairs room where it is warmest', 'keep as much rooms as possible closed to conserve heat',
                   'drink lots of warm liquids', 'wear baggy layered clothing']
        index = random.randint(0, len(advices)-1)
        selected_statement = Statement(text=advices[index])
        selected_statement.confidence = 1
        return selected_statement
