# dataset.py

benchmark_dataset = [

    # 5x5 environments
    {"scenario": "S1", "grid": 5, "obstacles": 3, "noise": 0.01, "steps": 100},
    {"scenario": "S2", "grid": 5, "obstacles": 3, "noise": 0.02, "steps": 100},
    {"scenario": "S3", "grid": 5, "obstacles": 3, "noise": 0.03, "steps": 100},
    {"scenario": "S4", "grid": 5, "obstacles": 3, "noise": 0.04, "steps": 100},
    {"scenario": "S5", "grid": 5, "obstacles": 3, "noise": 0.05, "steps": 100},

    # 10x10 environments
    {"scenario": "S6", "grid": 10, "obstacles": 7, "noise": 0.03, "steps": 300},
    {"scenario": "S7", "grid": 10, "obstacles": 7, "noise": 0.05, "steps": 300},
    {"scenario": "S8", "grid": 10, "obstacles": 7, "noise": 0.07, "steps": 300},
    {"scenario": "S9", "grid": 10, "obstacles": 7, "noise": 0.09, "steps": 300},

    # 15x15 environments
    {"scenario": "S10", "grid": 15, "obstacles": 12, "noise": 0.05, "steps": 600},
    {"scenario": "S11", "grid": 15, "obstacles": 12, "noise": 0.07, "steps": 600},
    {"scenario": "S12", "grid": 15, "obstacles": 12, "noise": 0.09, "steps": 600},
    {"scenario": "S13", "grid": 15, "obstacles": 12, "noise": 0.10, "steps": 600},

]