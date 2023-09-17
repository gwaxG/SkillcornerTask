import argparse
from src.calculus import Calculus

def get_file_path_from_arguments() -> str:
    """ Retireves data.log file path from the input arguments. 
    If no argument is provided, then the default path is used.

    Returns:
        str: data log file path.
    """

    parser = argparse.ArgumentParser(
        prog='Log parser',
        description='This is the Skillcorner first technical test solution.')
    
    parser.add_argument("-p", '--path')

    args = parser.parse_args()
    
    return args.path

def main():
    """ Defines data log file location and applies log parser on that file. """

    default_file_path = "data/data.log"

    arg_file_path = get_file_path_from_arguments()

    file_path = arg_file_path if arg_file_path is not None else default_file_path

    Calculus().read_lines(file_path).process_logs().show()

if __name__ == "__main__":
    main()
