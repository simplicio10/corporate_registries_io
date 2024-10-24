from typing import Optional
from pydantic import (
    BaseModel, 
    Field, 
    ConfigDict,
    field_validator)
from pathlib import Path
import logging
from cachetools import (
    cached, 
    LRUCache)
from rdflib import (
    URIRef, 
    Namespace)

logger = logging.getLogger(__name__)

class OntologyConfig(BaseModel):
    '''Stores IRIs and namespaces'''
    model_config = ConfigDict(arbitrary_types_allowed=True)

    il_prefix: str = Field(
        default='IL:',
        description='Prefix for Illinois entities'
        )
    vcard_prefix: str = Field(
        default='http://www.w3.org/2006/vcard/ns',
        description='Prefix for IRIs in VCard ontology'
        )
    soli_path: Path = Field(
        default=Path('../soli_ontology/soli.owl'),
        description='File path for forked version of ontology'
        )
    cache_dir: Path = Field(
        default=Path('.ontology_cache'),
        description='Directory for caching ontology info'
        )

    @field_validator('soli_path', 'cache_dir')
    @classmethod
    def validate_paths(cls, v: Path) -> Path:
        '''Convert string to path objects if needed'''
        if isinstance(v, str):
            return Path(v)
        if isinstance(v, Path):
            return v
        raise ValueError(f"Expected string or Path, got {type(v)}")

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
    model_config = ConfigDict(arbitrary_types_allowed=True, validate_assignment=True)

    config: OntologyConfig = Field(default_factory=OntologyConfig)
    IL_LLCs: Namespace = None
    VCARD: Namespace = None
    SOLI: Optional[str] = None
    
    def __init__(self, **data):
        '''Manages ontology namespaces and IRIs'''
        super().__init__(**data)
        self.initialize_ontology()

    def initialize_ontology(self) -> None:
        '''
        Initialize ontology namespaces and IRIs.

        config: optional configuration object. It defaults to the custom
        OntologyConfig class unless another config is provided.
        '''
        #Validate OWL file is in path
        if not self.config.soli_path.exists():
            raise OntologyError(f"OWL file not found at {self.config.soli_path}")
        #Creates cache directory if none exists
        self.config.cache_dir.mkdir(exist_ok=True)

        self.load_and_validate_ontology()

        #Initialize namespaces
        self.IL_LLCS = Namespace(self.config.il_prefix)
        self.VCARD = Namespace(self.config.vcard_prefix)
        self.SOLI = f"file://{self.config.soli_path.absolute()}"

    def load_and_validate_ontology(self) -> None:
        pass

    def get_entity_id_iri(self) -> URIRef:
        return URIRef(f"{self.SOLI}R955FuA1bPwrZWwF8Nc3v8A")

    def get_llc_iri(self) -> URIRef:
        return URIRef(f"{self.SOLI}R98E2kVwPFwTnP6oxYUt9HR")

if __name__ == "__main__":
    onto_test = Ontologies()