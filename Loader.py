import rhino3dm as rh
import tempfile

from zipfile import ZipFile

class Loader:
    
    def __init__(self):
        pass

    def Load(self, filePath):
        pass
    

    """

    """
    def IsADM(self, filePath):
        folder = tempfile.TemporaryDirectory()
        
        with ZipFile(filePath, 'r') as model:
            model.extractall()
        return False

    