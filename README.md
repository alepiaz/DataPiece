# Data Piece

Data Piece is a console-based application designed to streamline the process of data collection from the popular manga series, [One Piece](https://en.wikipedia.org/wiki/One_Piece). It provides an interactive interface for extracting detailed information from each chapter, page, and panel of the manga for data analysis purposes.

## Features

- Connects to a SQLite database.
- Handles database queries and executes SQL commands.
- Provides command completion options.
- Gracefully handles RuntimeErrors.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/alepiaz/datapiece.git
    ```
2. Navigate to the project directory:
    ```bash
    cd datapiece
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the console, run the following command:
```bash
python main.py --config config/config.json
```

## Database structure
![ERM](img/erd.png?raw=True)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT

