"""Compatibilidad de referencias inmutables tras sacar datos de la bóveda."""
from pathlib import Path
import os
import tempfile
import unittest
from unittest.mock import patch

from herramientas.rutas_trabajo import REPO, TRASLADOS, carpeta_trabajo, resolver_ruta, ruta_trabajo


class RutasTests(unittest.TestCase):
    def test_referencias_antiguas_absolutas_y_relativas(self):
        with tempfile.TemporaryDirectory() as temporary:
            with patch.dict(os.environ, {"LORCANA_TRABAJO": temporary}):
                for old, new in TRASLADOS.items():
                    target = Path(temporary) / new / 'fuente.json'
                    self.assertEqual(resolver_ruta(REPO / old / 'fuente.json'), target)
                    self.assertEqual(resolver_ruta(Path(old) / 'fuente.json'), target)
                    self.assertFalse(target.exists())  # No recurre al árbol antiguo.

    def test_no_traduce_notas_credenciales_ni_rutas_parecidas(self):
        for value in [REPO / '.env', REPO / 'Empecemos.md',
                      REPO / 'analisis/profesora-lorcana-otro/a.json',
                      REPO / 'analisis/discord-2026-09-05/a.json', Path('otro/a.json')]:
            self.assertEqual(resolver_ruta(value), value)

    def test_rechaza_destinos_dentro_de_la_boveda_y_escapes(self):
        for value in [str(REPO), str(REPO / 'analisis'), 'relativa']:
            with patch.dict(os.environ, {"LORCANA_TRABAJO": value}):
                with self.assertRaises(ValueError):
                    carpeta_trabajo()
        with tempfile.TemporaryDirectory() as temporary:
            with patch.dict(os.environ, {"LORCANA_TRABAJO": temporary}):
                with self.assertRaises(ValueError):
                    ruta_trabajo('../fuera.json')

    def test_consumer_verifica_bytes_sin_reescribir_referencia(self):
        from herramientas.duels_datos.catalogo import file_hash, verified_file
        import hashlib
        with tempfile.TemporaryDirectory() as temporary:
            with patch.dict(os.environ, {"LORCANA_TRABAJO": temporary}):
                old = REPO / 'analisis/profesora-lorcana/fuente.json'
                target = resolver_ruta(old)
                target.parent.mkdir(parents=True)
                target.write_bytes(b'{"original":true}')
                expected = hashlib.sha256(target.read_bytes()).hexdigest()
                self.assertEqual(file_hash(old), expected)
                self.assertEqual(verified_file(old, expected, 'gamelog', 'g')['status'], 'verified_json')
                target.write_bytes(b'{"original":false}')
                self.assertEqual(verified_file(old, expected, 'gamelog', 'g')['status'], 'hash_mismatch')


if __name__ == '__main__':
    unittest.main()
