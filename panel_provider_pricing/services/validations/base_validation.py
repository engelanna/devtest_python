import abc


class BaseValidation(abc.ABC):

   @abc.abstractmethod
   def passed(self):
      pass

   @abc.abstractmethod
   def error_message(self):
        pass
