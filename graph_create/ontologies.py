from rdflib import URIRef, Namespace
from soli import SOLI

class Ontologies:
    IL_LLCS = Namespace(":") #Custom Namespace ID
    VCARD = Namespace("http://www.w3.org/2006/vcard/ns") #VCard namespace for generic person and org concepts
    SOLI = SOLI()
    SOLI_IRI_PREFIX = "https://soli.openlegalstandard.org/"

    @classmethod
    def get_entity_id_iri(cls):
        return URIRef(f"{cls.SOLI_IRI_PREFIX}R955FuA1bPwrZWwF8Nc3v8A")

    @classmethod
    def get_llc_iri(cls):
        URIRef(f"{cls.SOLI_IRI_PREFIX}R98E2kVwPFwTnP6oxYUt9HR")