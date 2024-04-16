#Importing necessary packages
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader

import os

#Function to organize unstructured data from PDF
def get_index(data, index_name):
  index = None
  if not os.path.exists(index_name):
    print("building index", index_name)
    index = VectorStoreIndex.from_documents(data, show_progress=True)
    index.storage_context.persist(persist_dir=index_name)

  else:
    index = load_index_from_storage(
       StorageContext.from_defaults(persist_dir=index_name)
    )

  return index


pdf_path = os.path.join("data", "academicCalendar.pdf")
nsu_pdf = PDFReader().load_data(file=pdf_path)
nsu_index = get_index(nsu_pdf, "NSU")
nsu_engine = nsu_index.as_query_engine()