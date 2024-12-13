import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from unittest.mock import patch
from main import Main
from model import Document

def test_detect_document_type():
    run = Main()

    text_results = [
        [0, "Facture d'électricité"]
    ]
    document = run.detect_document_type(text_results)
    assert document._type == "Facture"
    
    text_results_banque = [
        [0, "Relevé bancaire"]
    ]
    document_banque = run.detect_document_type(text_results_banque)
    assert document_banque._type == "Banque"
    
    text_results_none = [
        [0, "Autre document"]
    ]
    document_none = run.detect_document_type(text_results_none)
    assert document_none is None

def test_process():
    run = Main()
    
    with patch.object(run, 'load_image') as mock_load, \
         patch.object(run, 'detect_document_type') as mock_detect, \
         patch.object(run, 'process_image') as mock_process, \
         patch.object(run, 'extract_data_from_image') as mock_extract:
        
        # Simuler les résultats à chaque étape
        mock_load.return_value = "mocked_image"
        mock_detect.return_value = Document("Facture")
        mock_process.return_value = {"scores": [0.95], "labels": [1], "boxes": [[0, 0, 10, 10]]}
        mock_extract.return_value = Document("Facture")
        
        # Exécuter le processus complet
        document = run.process("../documents/releve_banquaire.png")
        
        assert isinstance(document, Document)
        assert document._type == "Facture"
