class PackageStatus:
   TODO = "TODO"
   IN_PROGRES = "IN_PROGRES"
   DONE = "DONE"

   @classmethod
   def from_string(cls, status_string):
       if status_string not in [cls.TODO, cls.IN_PROGRES, cls.DONE]:
           raise ValueError(f"Wrong status {status_string}")
       return status_string
