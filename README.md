# Car-Project: Car Doors Component  

Welcome to the **Car-Project**, a modular initiative to develop a car from its components. This repository, **car-doors**, focuses on the car door functionalities and integrates automated testing using GitHub Actions to ensure code quality and reliability.  

## Features  

- **Core Functionality:**  
  - A `Door` class with methods to handle locking and other door-related operations.  

- **Automated Testing:**  
  - Uses Python's `unittest` module to validate functionality.  
  - Continuous Integration (CI) pipeline with GitHub Actions for automated testing on every push and pull request.  

- **Security Scans:**  
  - Planned integration with SonarQube for detecting code vulnerabilities during the merge process.  

---

## Repository Structure  

```plaintext
car-doors/
├── src/
│   └── door.py         # Implementation of the Door class
├── tests/
│   └── test_door.py    # Unit tests for Door functionality
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions workflow for automated testing
├── README.md           # Project documentation