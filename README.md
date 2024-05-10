# Thailand Panda Power Flow


This repository includes the code developed to simulate the power flow through the Thai electricity grid in 2024 and through a projected 2050 scenario.
This was built by the Thailand team for the 2024 Oxford MSc in Energy Systems Small Group Project.

We used the `PandaPower` module in Python using EGAT data.

Analysis is at a high level- we relied on the division of Thailand into four regions based on the four subdivisions that the Thai EGAT authority uses:
- North
- Northeast
- Central/Bangkok
- South

On top on these four nodes, we added the import and export nodes Thailand is connected to. Namely, imports from Laos and exports to Cambodia and Malaysia-Singapore.

  ##### **All input data is editable on `ThaiModelInput.xlsx`**

### File Structure: 
## Source Code

- **`README.md`**: Main documentation file providing an overview of the repository.
- **`LICENSE`**: License file specifying the terms of use for the code.
- **`.gitignore`**: File specifying which files and directories to ignore in version control.

- **`ThaiEnergyFlow.ipynb`**: Main source code for work in a Python Jupyter Notebook format. See this file to understand main analysis.
- **`ThaiModelInput.xlsx`**: An excel file with different sheets, with each one representing buses, lines, loads, and generation, with current valuesand 2050 projections. Change this file and the Jupyter notebook loops to change constraints.
- **`thai_power_calculations.xlsx`**: Additional calculations to understand projected constaints.
-  **`thai.shp` and `thai.shx`**: Shape files used to match coordinate graphing with lines and buses.
- **figures/**: We saved the main figures we used for our report here.
    - `2020_with_pink_upgrades`: figure that highlights where the pink color highlights where new lines must be added to ensure admissible 2050 constraints.  
    - `2050_with_voltage_upgrades`: figure that highlights high lines loads under higher 2050 generation and consumption loads.  

## Documentation
- **`simplifiedmap.pdf`** A 2020 map simplification of the broader Thai energy grid.
- **`thailand-grid-2001.md`**: Another regional glimpse into the Thai grid.
- **`api.md`**: API documentation.
- **`user-guide.md`**: User guide for using the software.
  
