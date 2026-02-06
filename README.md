# RBMK-Inspired Reactor & Turbine Simulator (Educational/Fictional)

This project is a **fictional, educational** RBMK-inspired reactor and turbine
simulator designed as a Python desktop game. All physics and values are
completely fictional, built for learning, gameplay, and systems thinking.

## Step 1 Scope
This first step focuses **only on project architecture and setup**. No
simulation logic is implemented yet — only folders, skeleton classes,
placeholders, and detailed documentation.

## Project Structure
```
Python-Graph-/
├── core/                  # Main simulation engine, time steps, logging
│   └── simulation.py
├── systems/               # Reactor, cooling, turbine, electrical stubs
│   ├── reactor.py
│   ├── cooling.py
│   ├── turbine.py
│   └── electrical.py
├── ui/                    # GUI placeholders (dashboard, gauges, alarms)
│   └── dashboard.py
├── tutorial/              # Tutorial and onboarding stubs
│   └── tutorial_manager.py
├── ai/                    # AI assistant/mentor stubs
│   └── assistant.py
├── scenarios/             # Scenario and challenge stubs
│   └── scenario_manager.py
├── mods/                  # Mod support stubs
│   └── mod_loader.py
├── utils/                 # Helper functions and config loader
│   ├── config.py
│   └── helpers.py
├── config.json            # Placeholder constants for tuning the simulator
└── README.md
```

## Conceptual Architecture
```
[Player Input]
     |
     v
[UI Panels] <------ [SimulationEngine] ------> [Systems Layer]
     ^                     |                         |
     |                     v                         v
 [Tutorial] <---------- [Logging] <----------- [Scenarios/AI]
```

## Design Notes
- **OOP-first:** Every subsystem is a class with placeholder lifecycle methods.
- **Central logging:** `core/simulation.py` owns logging setup for the project.
- **Debug-ready:** `SimulationSettings` includes a debug overlay flag for future
  UI integration.
- **Future-ready:** The structure anticipates full reactor physics, UI panels,
  tutorials, AI help, scenarios, and modding in later steps.

## Next Steps (Future)
- Implement fictional reactor physics and cooling loops.
- Add turbine/generator power logic.
- Build UI dashboards and alarm systems.
- Introduce tutorial scripts, AI advice, and scenario progression.
