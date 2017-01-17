from abc import ABCMeta, abstractmethod

class Property_Management(object):
      """Property Renting and To Let Services"""
      
      __metaclass__ = ABCMeta

      Deposit = 0
      No_of_Rooms = 0

      def __init__(self, location, Availability_Status):
            """Return a new Car Object"""
            self.location = location            
            self.Availability_Status = Availability_Status

      def Compute_ToLetPrices(self):
            """ Returns the monthly Letting amount to be paid by a customer"""
            if self.Availability_Status is None:
                  
                  return 10000 * self.No_of_Rooms

            elif self.Availability_Status is not None:
                  
                  return (10000 * self.No_of_Rooms) + self.Deposit

      def Compute_PropertyRentingPrice(self):
            """ Returns the Full Contract Amount to be paid to the premise owner"""
            if self.Availability_Status is None:
                  return 36 * (7000 * self.No_of_Rooms)
            else:
                  return 0.0

      @abstractmethod
      def Property_Type(self):
            """ Return type of Property"""
            pass

class Apartment(Property_Management):
      Deposit = 50000
      No_of_Rooms = 5

      def Property_Type(self):
            return 'Apartment'

class Maisonettes(Property_Management):
      Deposit = 40000
      No_of_Rooms = 4

      def Property_Type(self):
            return 'Maisonette'

      

      




                  
                  
