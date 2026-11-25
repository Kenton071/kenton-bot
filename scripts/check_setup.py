"""
Checks that every library is installed and benchmarks the evaluators.
Run:  python scripts/check_setup.py
"""

import importlib
import random
import sys
import time

REQUIRED = ["numpy", "numba", "pandas", "phevaluator", "matplotlib", "tqdm", "pytest", "kentonbot"]
OPTIONAL = ["eval7"]
RANKS, SUITS = "23456789TJQKA", "cdhs"


def check_imports() -> bool:
    ok = True
    print(f"Python {sys.version.split()[0]}")
    for name in REQUIRED + OPTIONAL:
        try:
            mod = importlib.import_module(name)
            print(f"  [ok]       {name:<12} {getattr(mod, '__version__', '')}")
        except ImportError:
            optional = name in OPTIONAL
            print(f"  [{'optional' if optional else 'MISSING '}] {name}")
            ok = ok and optional
    return ok


def bench(label, fn, hands):
    t = time.perf_counter()
    for h in hands:
        fn(h)
    rate = len(hands) / (time.perf_counter() - t)
    print(f"  {label:<18} {rate:>12,.0f} hands/sec")


def benchmark(n: int = 30_000) -> None:
    rng = random.Random(0)
    hands = [rng.sample(range(52), 7) for _ in range(n)]
    print(f"\nEvaluator speed ({n:,} random 7-card hands):")

    try:
        from kentonbot.evaluator import evaluate7
        evaluate7(hands[0])
        bench("kentonbot (yours)", evaluate7, hands)
    except NotImplementedError:
        print("  kentonbot (yours)  not written yet")

    from phevaluator import evaluate_cards
    strs = [[RANKS[c >> 2] + SUITS[c & 3] for c in h] for h in hands]
    bench("phevaluator", lambda h: evaluate_cards(*h), strs)

    try:
        import eval7
        cards = [[eval7.Card(RANKS[c >> 2] + SUITS[c & 3]) for c in h] for h in hands]
        bench("eval7 (C)", eval7.evaluate, cards)
    except ImportError:
        pass


if __name__ == "__main__":
    ok = check_imports()
    if ok:
        benchmark()
    print("\nSetup looks good." if ok else "\nSome required libraries are missing; rerun setup.")
    sys.exit(0 if ok else 1)
