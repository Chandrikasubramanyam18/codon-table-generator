import subprocess
import sys
import unittest


class TestCodonTableGenerator(unittest.TestCase):

    def run_program(self, user_input):
        result = subprocess.run(
            [sys.executable, "main.py"],
            input=user_input,
            text=True,
            capture_output=True
        )
        return result.stdout

    def test_dna_translation(self):
        output = self.run_program("DNA\nATGGCTTTTTAA\n")
        self.assertIn("Methionine", output)
        self.assertIn("Alanine", output)
        self.assertIn("Phenylalanine", output)
        self.assertIn("Stop", output)

    def test_rna_input(self):
        output = self.run_program("RNA\nAUGGCUUUUUAA\n")
        self.assertIn("Methionine", output)
        self.assertIn("DNA sequence: ATGGCTTTTTAA", output)

    def test_invalid_sequence(self):
        output = self.run_program("DNA\nATGBBB\n")
        self.assertIn("Invalid DNA sequence", output)

    def test_incomplete_codon(self):
        output = self.run_program("DNA\nATGGCTTTTAA\n")
        self.assertIn("Incomplete codon: AA", output)


if __name__ == "__main__":
    unittest.main()
    