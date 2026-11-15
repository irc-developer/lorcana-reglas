import json
from pathlib import Path
import tempfile
import unittest

from herramientas.profesora_lorcana.contratos import (
    canonical, check_reference, digest, file_digest, read, reference,
)


class ContractTests(unittest.TestCase):
    def test_formatting_changes_bytes_but_not_identity(self):
        value = {'schema': 'lorcana-position-v1', 'texto': 'acción', 'a': [1, False, None]}
        with tempfile.TemporaryDirectory() as temporary:
            a, b = Path(temporary) / 'a.json', Path(temporary) / 'b.json'
            a.write_text(json.dumps(value, ensure_ascii=False), encoding='utf-8')
            b.write_text(json.dumps(value, sort_keys=True, indent=4), encoding='utf-8')
            self.assertNotEqual(file_digest(a), file_digest(b))
            self.assertEqual(reference(read(a)), reference(read(b)))

    def test_content_change_invalidates_reference(self):
        original = {'schema': 'lorcana-diagnosis-v1', 'assessment': 'defendible'}
        changed = {**original, 'assessment': 'indeterminada'}
        check_reference(reference(original), original)
        with self.assertRaises(ValueError):
            check_reference(reference(original), changed)

    def test_duplicate_keys_and_nonfinite_values_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'input.json'
            for invalid in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
                path.write_text(invalid, encoding='utf-8')
                with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                    read(path)
        with self.assertRaises(ValueError):
            digest({'a': float('nan')})

    def test_non_json_python_shapes_are_rejected(self):
        for value in ({1: 'value'}, {'a': (1, 2)}, {'a': {1, 2}}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                canonical(value)

    def test_reference_shape_has_no_paths_or_byte_hash(self):
        artifact = {'schema': 'lorcana-choice-v1', 'observed_action': 'a'}
        self.assertEqual(set(reference(artifact)), {'schema', 'sha256'})
        with self.assertRaises(ValueError):
            check_reference({**reference(artifact), 'path': 'original.json'}, artifact)


if __name__ == '__main__':
    unittest.main()
