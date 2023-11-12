# ZCMC-IHOMP BorrowMe V1.0.0


BorrowMe is a Django-based web application created using Python that allows ZCMC employees to check the availability of peripheral devices and proceed to borrow them.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Browse available peripheral devices.
- Request to borrow devices.
- Admin panel for managing device availability.

## Installation

### Prerequisites

- Python 3.x
- Django
- Other dependencies (list in requirements.txt)

### Instructions

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/ZCMC-IHOMP-BorrowMe.git

2. Install the project dependencies:
    - pip install -r requirements.txt

3. Migrate the database:
    - python manage.py makemigrations
    - python manage.py migrate

4. Start the development server:
    - python manage.py runserver

5. Access the application in your web browser at http://localhost:8000/.

## Usage

1. Browse the available peripheral devices.
2. Click on a device to view details and request to borrow it.
3. Admins can log in and manage device availability through the admin panel at http://localhost:8000/admin/.

## Contributing
We welcome contributions from the community. If you'd like to contribute to ZCMC-IHOMP BorrowMe, please follow these steps:

Fork the repository.
1. Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name or bugfix/your-bug-fix.
2. Make your changes and commit them.
3. Push your changes to your fork: git push origin feature/your-feature-name.
4. Create a pull request on the main repository's main branch.
