"""Static release integrity and basic defensive-surface checks. No external libraries."""
import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.s=(ROOT/"index.html").read_text(encoding="utf-8")
    def test_standalone_copy(self):
        self.assertEqual((ROOT/"index.html").read_bytes(),(ROOT/"TAFL_ATLAS_Offline_v1.0.html").read_bytes())
    def test_csp(self):
        for directive in ("default-src 'none'","connect-src 'none'","object-src 'none'","base-uri 'none'"): self.assertIn(directive,self.s)
    def test_no_external_scripts_styles(self):
        self.assertNotRegex(self.s,r"<script[^>]+src\s*=")
        self.assertNotRegex(self.s,r"<link[^>]+href\s*=")
        self.assertNotRegex(self.s,r"@import\s")
    def test_no_network_apis(self):
        for expr in (r"\bfetch\s*\(",r"new\s+(?:XMLHttpRequest|WebSocket|EventSource)\s*\("):
            self.assertNotRegex(self.s,expr)
    def test_script_single(self):
        self.assertEqual(len(re.findall(r"<script\b",self.s,re.I)),1)
    def test_protocol(self):
        for item in ("TA2.","function decode(","function replay("): self.assertIn(item,self.s)
    def test_board_geometry(self):
        self.assertIn("grid-template-rows:",self.s)
        self.assertIn("Moving a piece does not alter row height",self.s)
    def test_version(self):self.assertIn("TAFL ATLAS v1.0.0",self.s)
if __name__=="__main__":unittest.main()
