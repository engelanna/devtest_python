class BaseValidation():

    def __init__(self):
        self.error_messages = []


    def errors_as_a_sentence(self):
        return ". ".join(self.error_messages)

    def passed(self):
        passsed = True

        for param in self.required_params.keys():
            if not param:
                passed = False
                self.error_messages.append(f"Missing parameter: {param}")

        return passed

