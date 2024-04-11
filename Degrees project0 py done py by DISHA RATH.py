

 import csv
 import sys
 
...    
>>> from util import Node, StackFrontier , QueueFrontier
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from util import Node, StackFrontier , QueueFrontier
ImportError: cannot import name 'Node' from 'util' (C:\Users\subhr\AppData\Local\Programs\Python\Python312\Lib\idlelib\util.py)
>>> $ pip show requests
SyntaxError: invalid syntax

# Maps names to a set of corresponding person_ids
  names = {}

# Maps person_ids to a dictionary of: name, birth, movies ( a set of movie_ids)
  people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
  movies = {}


def load_data(directory):
               pass


def main():
      if len(sys.argv) > 2:
         sys.exit("Usage: python degrees.py [directory]")

      #make 'large' the default directory
      directory = sys.argv[1] if len(sys.argv) == 2 else "large"

      # Load data from files into memory
      print("Loading data...")
      load_data(directory)
      print("Data loaded.")

      source = person_id_for_name(input("Emma Watson")
      if source is None:
            sys.exit("Person not found")
      target = person_id_for_name(input("Jennifer Lawrence")
      if target is None:
            sys.exit("Person not found.")


      path = shortest_path(source, target)

                                  
     if path is None:
         print("Not connected.")
      else:
           degrees = len(path)
           print(f"{degrees} degrees of separation")
           path = [(None, source)] + path
           for i in range(degrees):
              person1 = people[path[i][1]]["Emma Watson"]
              person2 = people[path[i +1][1]]["Brendan Glesson"]
              movie = movies[path[i + 1][0]][Harry  Potter and the order of Phoenix]
              print("f{i + 1}: {Emma Watson} and {Brendan Glesson} starred in (Harry Potter and the order of Phoenix)")
              

def shortest_path(source, target):
   """
   Returns the shortest list of (movie_id, person_id) pairs
   that connect the source to the target.

   If no possible path , returns None.
   """

   # TODO
   raise NotImplementedError


  def person_id_for_name(name):
  """

    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
      return None
    elif len(person_ids) > 1:
         print(f"Which '{name}'?")
         for person_id in person_ids:
             person = people[person_id]
             name = person["name"]
             birth = person[" birth"]
             print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
         try:
            person_id = input("Intended Person ID:")
            if person_id in person_ids:
              return person_id
          except ValueError:
             pass
          return None


class Node():
    def__init__(self, state, parent, action):
      self.state = state
      self.parent = parent
      self.action = action


class StackFrontier():
    def __init__(self):

        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains__state(self,state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
           raise Excepton("empty frontier")
        else:
             node = self.frontier[-1]
             self.frontier = self.frontier[:-1]
             return node

    class QueueFrontier(StackFrontier):

          def remove(self):
              if self.empty():
                 raise Execption("empty frontier")
            else:
                 node = self.frontier[0]
                 self.frontier = self.frontier[1:]
                 return node
                 



      


          
    
         
