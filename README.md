# kenton-bot
bot that plays like kenton mit freshman

A poker bot built from simulation and game-theory math, starting with **preflop** in No-Limit Texas Hold'em.

---

## Setup

You need **Python 3.10+** ([python.org](https://www.python.org/downloads/)) and git.

```bash
git clone https://github.com/Kenton071/kenton-bot.git
cd kenton-bot
```

**Mac / Linux**
```bash
bash setup.sh
source .venv/bin/activate        # every time you open a new terminal
```

**Windows (PowerShell)**
```powershell
.\setup.ps1
.\.venv\Scripts\Activate.ps1     # every time you open a new terminal
```

The setup script creates a virtual environment in `.venv`, installs everything, and runs `scripts/check_setup.py` to confirm it worked.

### Libraries

| Library | What it's for |
|---|---|
| `numpy` | Fast arrays: equity matrices, strategy tables |
| `numba` | Compiles hot Python loops to machine code (10-100x speedups for simulation) |
| `pandas` | Tables of results, range charts |
| `phevaluator` | Trusted hand evaluator: check yours against it, or use it for speed |
| `eval7` *(optional)* | C-based evaluator, fastest option |
| `matplotlib` | Plots: convergence, equity heatmaps |
| `jupyterlab` | Notebooks for experiments (`jupyter lab`) |
| `tqdm` | Progress bars for long simulations |
| `pytest` | Tests that tell you when each step works |

---

## Project layout

```
kentonbot/          your code
  cards.py          step 1: card encoding
  evaluator.py      step 2: 7-card hand evaluator
  ranges.py         step 3: range notation -> combos
  equity.py         step 4: Monte Carlo equity
tests/              one test file per step - make them pass
scripts/            check_setup.py (installs + evaluator benchmark)
notebooks/          experiments
data/               generated data (big files are git-ignored)
```

Each file in `kentonbot/` contains an outline: function signatures, what they should return, and hints. Replace each `raise NotImplementedError` with your own code.

## Workflow

```bash
pytest tests/test_cards.py        # test just the step you're on
pytest                            # everything
python scripts/check_setup.py     # see how fast your evaluator is vs the libraries
```

All tests fail at the start. That's expected: each test is the target for one step.

---

## Plan

### Phase 1: Equity engine (preflop foundation)
- [ ] **Step 1 - Cards:** encode cards as ints 0-51 (`tests/test_cards.py`)
- [ ] **Step 2 - Evaluator:** score any 7 cards so a higher score always wins (`tests/test_evaluator.py`)
- [ ] **Step 3 - Ranges:** parse `QQ+, ATs+, AKo` into combos (`tests/test_ranges.py`)
- [ ] **Step 4 - Monte Carlo equity:** hand/range vs range, with error bars (`tests/test_equity.py`)
- [ ] **Step 5 - Speed:** use numba or a library evaluator, then precompute the 169x169 preflop equity matrix into `data/`

### Phase 2: Preflop GTO
- [ ] **Step 6 - Push/fold solver:** heads-up shove/call ranges at 5-15bb with fictitious play or CFR; check against published Nash charts
- [ ] **Step 7 - Exploitability:** best-response calculator to measure how far a strategy is from GTO
- [ ] **Step 8 - Heads-up 100bb preflop:** open / 3-bet / 4-bet tree with CFR+, using equity x realization factor for postflop
- [ ] **Step 9 - Bet sizing:** compare EV and exploitability across different size menus

### Phase 3: Play like Kenton
- [ ] **Step 10 - Record hands:** log your own decisions (position, stacks, hand, action)
- [ ] **Step 11 - Compare to GTO:** where your play deviates from the solver, and what it costs in bb/100
- [ ] **Step 12 - Kenton model:** GTO baseline + your tendencies (imitation learning on your hand history)
- [ ] **Step 13 - 6-max positions, then postflop streets**

---

## Key formulas

```
Pot odds (equity needed to call):  B / (P + B)          P = pot incl. villain's bet, B = amount to call
EV of call:                        R·E·(P + B) − B       E = equity, R = realization factor
EV of raise:                       f·P + (1−f)·[E_called·(P + S + C) − S]
Minimum defense frequency:         P / (P + B)
Monte Carlo standard error:        sqrt(p(1−p) / N)
Combos:                            pair 6, suited 4, offsuit 12, total 1326
```
