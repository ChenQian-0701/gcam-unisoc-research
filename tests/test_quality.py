import importlib.util,unittest
from pathlib import Path
import numpy as np
spec=importlib.util.spec_from_file_location('compare',Path(__file__).resolve().parents[1]/'tools/quality/compare_jpegs.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class OutputNoiseTest(unittest.TestCase):
    def test_known_random_noise_with_brightness_and_gradient_drift(self):
        rng=np.random.default_rng(123)
        x=np.linspace(-1,1,96)[None,None,:]
        drift=np.arange(12)[:,None,None]*3
        a=100+drift+np.arange(12)[:,None,None]*x+rng.normal(0,2,(12,96,96))
        b=100+drift+np.arange(12)[:,None,None]*x+rng.normal(0,1,(12,96,96))
        ma=mod.measure(a);mb=mod.measure(b)
        self.assertAlmostEqual(ma['temporal_plane_corrected'],2,delta=.04)
        self.assertAlmostEqual(mb['temporal_plane_corrected'],1,delta=.03)
        self.assertAlmostEqual(mb['temporal_plane_corrected']/ma['temporal_plane_corrected'],.5,delta=.025)
        self.assertGreater(ma['temporal_raw'],ma['temporal_plane_corrected']*2)

if __name__=='__main__':unittest.main()
