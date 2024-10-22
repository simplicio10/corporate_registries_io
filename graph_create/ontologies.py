from typing import Optional
from pydantic import BaseModel
from pathlib import Path
from cachetools import cached, LRUCache
from rdflib import URIRef, Namespace



class OntologyConfig(BaseModel):
    '''Config file to store ontology IRIs and namespaces'''
    soli_path: str = '../soli_ontology/soli.owl' #Forked version of ontology
    il_prefix: str = "IL:"
    vcard_prefix: str = "http://www.w3.org/2006/vcard/ns"
    cache_dir: str = '.ontology_cache' #Directory for caching ontology info

class OntologyError(Exception): #Refactor
    '''Base exception for ontology-related errors'''
    pass

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

    

        
    
    IL_LLCS = Namespace("IL:") #Custom Namespace ID
    VCARD = Namespace("http://www.w3.org/2006/vcard/ns") #VCard namespace for generic person and org concepts
    SOLI_IRI_PREFIX = "https://soli.openlegalstandard.org/"

    @classmethod
    def get_entity_id_iri(cls):
        return URIRef(f"{cls.SOLI_IRI_PREFIX}R955FuA1bPwrZWwF8Nc3v8A")

    @classmethod
    def get_llc_iri(cls):
        return URIRef(f"{cls.SOLI_IRI_PREFIX}R98E2kVwPFwTnP6oxYUt9HR")

if __name__ == "__main__":
    print(Ontologies.get_entity_id_iri())
    print(Ontologies.get_llc_iri())