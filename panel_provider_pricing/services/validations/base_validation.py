import abc


class BaseValidation(abc.ABC):

   @abc.abstractmethod
   def passed(self):
      pass
