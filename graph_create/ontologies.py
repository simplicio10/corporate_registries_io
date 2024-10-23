from typing import Optional
from pydantic import BaseModel, Field
from pathlib import Path
import logging
from cachetools import cached, LRUCache
from rdflib import URIRef, Namespace

logger = logging.getLogger(__name__)

class OntologyConfig(BaseModel):
    '''Stores IRIs and namespaces'''
    il_prefix: str = Field(
        default='IL:',
        description='Prefix for Illinois entities'
        )
    vcard_prefix: str = Field(
        default='http://www.w3.org/2006/vcard/ns',
        description='Prefix for IRIs in VCard ontology'
        )
    soli_path: str = Field(
        default='../soli_ontology/soli.owl',
        description='File path for forked version of ontology'
        )
    cache_dir: str = Field(
        default='.ontology_cache'
        description='Directory for caching ontology info'
        ) 

class OntologyError(Exception): #Refactor
    '''Base exception for ontology-related errors'''
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class InvalidIRIError(OntologyError): #Refactor
    pass

class OntologyFileError(OntologyError): #Refactor
    pass

class Ontologies(BaseModel):
    '''Manages ontology namespaces and IRIs for Illinois corporate entities'''
    
    def __init__(self, config: Optional[OntologyConfig] = None):
        '''
        Initialize ontology namespaces and IRIs.

        config: optional configuration object. It defaults to the custom
        OntologyConfig class unless another config is provided.
        '''
        self.config = config if config is not None else OntologyConfig()
        self.soli_owl_path = Path(self.config.soli_path)

        if not self.soli_owl_path.exists():
            raise OntologyError(f"OWL file not found at {self.soli_owl_path}")
        
        self.cache_dir = Path(self.config.cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

        self.load_and_validate_ontology()

        #Initialize namespaces
        self.IL_LLCS = Namespace(self.config.il_prefix)
        self.VCARD = Namespace(self.config.vcard_prefix)
        self.SOLI = f"file://{self.soli_owl_path.absolute()}"

    def load_and_validate_ontology(self) -> None:
        pass

    @classmethod
    def get_entity_id_iri(cls):
        return URIRef(f"{cls.SOLI}R955FuA1bPwrZWwF8Nc3v8A")

    @classmethod
    def get_llc_iri(cls):
        return URIRef(f"{cls.SOLI}R98E2kVwPFwTnP6oxYUt9HR")

if __name__ == "__main__":
    onto_test = Ontologies()