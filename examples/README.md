## Examples:
- `examples/` - Basic usage examples (.pyn and .py)
- `examples/test_luce/` - Edge-case stress tests  
- `examples/test_ru/` - Architectural scale tests
- `case_study/` - in-field real use cases

## Quick Test:
# Test pyndent on Ru's complex examples
pyndent examples/test_ru/chaos_1_500.pyn -o temp.py && python temp.py
