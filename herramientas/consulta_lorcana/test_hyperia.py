"""Vigencia e integridad de las fuentes y erratas de Hyperia City."""
from datetime import date
from pathlib import Path
import tempfile
import json
from contextlib import closing
import unittest
from unittest.mock import patch
import core as x


class HyperiaTests(unittest.TestCase):
    def test_cached_cards_change_when_effective_date_is_crossed(self):
        base=x.HERE/'.cache'
        with tempfile.TemporaryDirectory(prefix='test-errata-date-',dir=base) as tmp:
            folder=Path(tmp).resolve()
            self.assertTrue(folder.is_relative_to(base.resolve()))
            db=folder/'indice.sqlite'
            with patch.object(x,'fecha_local',return_value=date(2026,10,15)):
                x.update(x.ROOT,db)
                with closing(x.ro_connection(db)) as c:
                    previous=next(json.loads(r[0]) for r in c.execute("select payload from chunks where kind='card'") if json.loads(r[0])['title']=='Jukebox')
            with patch.object(x,'fecha_local',return_value=date(2026,10,16)):
                self.assertFalse(x.freshness(x.ROOT,db)['current'])
                x.update(x.ROOT,db)
                with closing(x.ro_connection(db)) as c:
                    current=next(json.loads(r[0]) for r in c.execute("select payload from chunks where kind='card'") if json.loads(r[0])['title']=='Jukebox')
                self.assertTrue(x.freshness(x.ROOT,db)['current'])
            self.assertEqual(previous['operative_text_status'],'impreso_previo')
            self.assertEqual(current['operative_text_status'],'corregido_oficial')
            self.assertIn('same name as another card',current['operative_ability'])

    def card(self, day, name='Jukebox'):
        config=x.load_json(x.HERE/'fuentes.json')
        spec=next(s for s in config['card_errata'] if s['name']==name)
        with patch.object(x,'fecha_local',return_value=day):
            chunks,_=x.parse_source(x.ROOT,spec['path'],dict(kind='card',scope='estandar'),{})
        return next(c for c in chunks if c['title']==name)

    def test_jukebox_boundary_preserves_literal_source(self):
        previous=self.card(date(2026,10,15));current=self.card(date(2026,10,16))
        self.assertIn('same name as a card',previous['operative_ability'])
        self.assertIn('same name as another card',current['operative_ability'])
        self.assertEqual(previous['text'],current['text'])
        self.assertEqual(previous['raw_text'],current['raw_text'])
        self.assertEqual(current['operative_text_status'],'corregido_oficial')

    def test_no_invented_full_adventurous_text(self):
        for name in ['Gaston - Frightful Bully','Cobra Bubbles - Dedicated Official',
                     'Ariel - Curious Traveler','This Growing Pressure','Woody - Town Sheriff']:
            with self.subTest(name=name):
                c=self.card(date(2026,10,16),name)
                self.assertIsNone(c['operative_ability'])
                self.assertEqual(c['operative_text_status'],'nueva_redaccion_completa_no_publicada')
                self.assertIn('Adventurous',c['operative_clarification'])

    def test_official_notes_registered_with_verified_hashes(self):
        entries,selection=x.inventory(x.ROOT)
        rel='Documentacion Oficial/Hyperia-City-Set-Release-Notes_EN.md'
        self.assertEqual(entries[rel]['authority'],'notas_oficiales')
        chunks,meta=x.parse_source(x.ROOT,rel,entries[rel],selection)
        self.assertIn('/hyperia-city-set-release-notes',meta['official_link']['url'])
        self.assertTrue(any('Bauble Game' in c['text'] for c in chunks))
        self.assertEqual(sum(c['text'].count('Q:') for c in chunks),26)

    def test_altered_original_rejected(self):
        real=x.digest
        def altered(data):
            if b'Disney Lorcana TCG Set Release Notes: Hyperia City' in data and data.startswith(b'<!'):
                return '0'*64
            return real(data)
        with patch.object(x,'digest',side_effect=altered):
            with self.assertRaisesRegex(ValueError,'Fuente oficial modificada'):
                x.inventory(x.ROOT)

    def test_current_policies_replace_previous_tournament_copy(self):
        entries, selection = x.inventory(x.ROOT)
        old = 'Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf'
        self.assertEqual(entries[old]['kind'], 'excluded')
        for name, kind in [('Tournament-Rules-7.14.2026_Update_EN.pdf', 'tournament'),
                           ('Disney_Lorcana_Play_Correction_Guidelines_052124update.pdf', 'correction')]:
            rel = 'Documentacion Oficial/' + name
            self.assertEqual(entries[rel]['kind'], kind)
            self.assertEqual(entries[rel]['authority'], 'politica_oficial')
            self.assertEqual(x.digest((x.ROOT / rel).read_bytes()),
                             x.load_json(x.HERE / 'fuentes.json')['verified_urls'][name]['sha256'])


if __name__=='__main__':
    unittest.main()
