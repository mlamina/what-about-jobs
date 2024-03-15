# What About Jobs?

## Overview
This project, `what-about-jobs`, aims to address the critical question of how society can adapt to the challenges and opportunities presented by artificial intelligence (AI) in the labor market. Specifically, it seeks to iteratively solve the problem of AI replacing human labor, exploring ways to reform society to ensure a future where everyone thrives alongside AI.

The project is built around an AI agent system with the following key properties:
- **File-based**: All results are stored as Markdown files within the repository, ensuring transparency and accessibility.
- **Iterative**: Utilizes an `iterate.py` script for running new iterations that improve our current solution to the problem.
- **Self-Aware**: The system can locate and understand its own code, enhancing its ability to adapt and evolve.
- **Reflective**: It leverages the results of previous iterations and its understanding of its own code to further refine solutions.
- **Self-Improving**: Each iteration assesses the need for adjustments within the agent system itself.

The project employs `langchain` for the agent system and ensures all Python code is unit-tested using pytest and tox on Python 11, with tests running via a GitHub action.

## Getting Started
To get started with the `what-about-jobs` project, follow these steps:

1. **Clone the Repository**
   Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/mlamina/what-about-jobs.git
   ```
2. **Set Up Your Environment**
   Ensure you have Python 11 installed. Set up a virtual environment and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the `iterate.py` Script**
   To run an iteration, execute the `iterate.py` script:
   ```bash
   python iterate.py
   ```

## Contributing
Contributions are welcome! If you have ideas on how to improve the project or want to contribute code, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.