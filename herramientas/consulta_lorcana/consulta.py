"""Entrada sin bytecode: una consulta nunca crea cachés Python."""
import sys
sys.dont_write_bytecode = True
from core import main

if __name__ == "__main__":
    raise SystemExit(main())
