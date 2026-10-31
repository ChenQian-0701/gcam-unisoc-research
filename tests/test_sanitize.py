import importlib.util,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('sanitize',Path(__file__).resolve().parents[1]/'tools/privacy/sanitize.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class RedactionTest(unittest.TestCase):
    def test_private_fields_and_explicit_unlabelled_identifier(self):
        source='/home/alice/file serial=PRIVATE123\nMAC=aa:bb:cc:dd:ee:ff\nIP=192.168.1.2\nGPSLatitude=31.23\ncontact=person@example.com\nPRIVATE123'
        result=mod.sanitize(source,['PRIVATE123'])
        for value in ['alice','PRIVATE123','aa:bb:cc:dd:ee:ff','192.168.1.2','31.23','person@example.com']:
            self.assertNotIn(value,result)
    def test_camera_measurements_are_retained(self):
        text='exp_ns=20000000 iso=163 sensor_ts=54040300312597 accepted=true version=9.6.080.695519101.19'
        self.assertEqual(mod.sanitize(text),text)

if __name__=='__main__':unittest.main()
