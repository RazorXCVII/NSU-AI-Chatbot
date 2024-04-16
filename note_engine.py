#Importing necessary packages
from llama_index.core.tools import FunctionTool
import os

#Specifying path to notes.txt file
note_file = os.path.join("data", "notes.txt")

#Function to Save/Update note file
def save_note(note):
  #Will create new file if it doesn't exist
  if not os.path.exists(note_file):
    open(note_file, "w")

  #If file exists, it will update it  
  with open(note_file, "a") as n:
    n.writelines([note + "\n"])
  
  return "Note has been successfully Saved"

#Initilizing note editing tool
note_engine = FunctionTool.from_defaults(
  fn = save_note,
  name = "Note_editor",
  description = "This tool can create or update a text based note file by taking notes from the user"
)