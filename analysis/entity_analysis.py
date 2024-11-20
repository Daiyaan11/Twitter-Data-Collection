import nltk
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_named_entities(text):
    """Extract named entities (people, locations, organizations) from text."""
    tokens = nltk.word_tokenize(text)
    pos_tags = pos_tag(tokens)
    chunks = ne_chunk(pos_tags)
    
    entities = {"PERSON": [], "ORGANIZATION": [], "LOCATION": []}
    for chunk in chunks:
        if isinstance(chunk, Tree):
            entity = " ".join(c[0] for c in chunk)
            entity_type = chunk.label()
            if entity_type in entities:
                entities[entity_type].append(entity)
    
    return entities
