# Aprilo in Cursor per attivare la regola test-pytest.mdc
import pytest

from prezzi import applica_sconto


@pytest.mark.parametrize("prezzo, perc, atteso", [(100, 10, 90), (50, 0, 50), (80, 100, 0)])
def test_applica_sconto(prezzo, perc, atteso):
    assert applica_sconto(prezzo, perc) == atteso


def test_percentuale_non_valida():
    with pytest.raises(ValueError):
        applica_sconto(100, 150)
