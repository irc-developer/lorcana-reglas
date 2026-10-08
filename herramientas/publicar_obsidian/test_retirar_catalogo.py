"""La retirada solo admite fichas explícitas y conserva el corpus local."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import tempfile
import unittest

import publicar as p
import retirar_catalogo as r


class RetiradaTests(unittest.TestCase):
    def test_seleccion_acotada_y_entrada_conservada(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ficha = "02. Listado de Cartas/Set 1 - The First Chapter.md"
            path = root / ficha
            path.parent.mkdir()
            path.write_bytes(b"Corpus intacto\n")
            selected = r.preparar_retirada(root, [ficha], {ficha, r.ENTRADA})
            self.assertTrue(selected[ficha]["publicada"])
            self.assertEqual(path.read_bytes(), b"Corpus intacto\n")
            for invalid in ([r.ENTRADA], ["../Set 1.md"], [ficha, ficha], [],
                            ["01. Reglas/Set 1.md"], ["02. Listado de Cartas/Otra nota.md"]):
                with self.subTest(invalid=invalid), self.assertRaises(p.PublicacionError):
                    r.preparar_retirada(root, invalid, {ficha})


if __name__ == "__main__":
    unittest.main(verbosity=2)
