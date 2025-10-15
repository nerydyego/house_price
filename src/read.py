import pandas as pd
from charset_normalizer import from_path as fr
from pathlib import Path


def detect_file_encoding(file_path: Path | str) -> tuple[str, float]:
    """Detecta o encoding de um arquivo usando charset_normalizer.

    Args:
        file_path: Caminho do arquivo a ser analisado.

    Returns:
        Tuple (encoding, confidence) onde:
            - encoding: nome da codificação detectada (ex.: 'utf_8', 'iso-8859-1').
            - confidence: confiança (0.0 a 1.0).

    Raises:
        FileNotFoundError: se o arquivo não existir.
        ValueError: se não for possível determinar um encoding.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    resultado = fr(path).best()

    if not resultado or not resultado.encoding:
        raise ValueError(f"Não foi possível detectar o encoding do arquivo {path}")

    return resultado.encoding, resultado.chaos

