"""
Logging utilities for Greenland Sea ice study.

Provides consistent logging across all analysis scripts with:
- Timestamped log files
- Multiple output streams (file + console)
- Structured log entries
- Automatic log directory creation
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
import yaml


def setup_logger(script_name, config_path='config.yaml', log_level=None):
    """
    Set up a logger for an analysis script.
    
    Parameters
    ----------
    script_name : str
        Name of the script/notebook (e.g., 'figure_01')
    config_path : str or Path
        Path to config.yaml file
    log_level : str, optional
        Logging level (DEBUG, INFO, WARNING, ERROR). 
        If None, reads from config.
    
    Returns
    -------
    logging.Logger
        Configured logger instance
    """
    # Load configuration
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Get log level from config if not specified
    if log_level is None:
        log_level = config.get('processing', {}).get('log_level', 'INFO')
    
    # Create logs directory if it doesn't exist
    log_dir = Path(config['paths']['logs'])
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create timestamped log filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f"{script_name}_{timestamp}.log"
    
    # Create logger
    logger = logging.getLogger(script_name)
    logger.setLevel(getattr(logging, log_level))
    
    # Remove existing handlers (in case of re-initialization)
    logger.handlers.clear()
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    console_formatter = logging.Formatter(
        '%(levelname)-8s | %(message)s'
    )
    
    # File handler (detailed logging)
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    logger.addHandler(file_handler)
    
    # Console handler (less verbose)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # Log initialization
    logger.info("=" * 70)
    logger.info(f"Starting analysis: {script_name}")
    logger.info(f"Log file: {log_file}")
    logger.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 70)
    
    return logger


def log_data_loading(logger, data_source, filepath, dims=None, time_range=None):
    """
    Log data loading information.
    
    Parameters
    ----------
    logger : logging.Logger
        Logger instance
    data_source : str
        Name of data source (e.g., 'ERA5', 'OSISAF')
    filepath : str or Path
        Path to data file(s)
    dims : dict, optional
        Dictionary of dimension sizes
    time_range : tuple, optional
        (start, end) of time coverage
    """
    logger.info(f"Loading {data_source} data from: {filepath}")
    
    if dims:
        dims_str = ", ".join([f"{k}: {v}" for k, v in dims.items()])
        logger.info(f"  Dimensions: {dims_str}")
    
    if time_range:
        logger.info(f"  Time range: {time_range[0]} to {time_range[1]}")


def log_processing_step(logger, step_name, details=None):
    """
    Log a processing step.
    
    Parameters
    ----------
    logger : logging.Logger
        Logger instance
    step_name : str
        Name of processing step
    details : dict, optional
        Additional details about the step
    """
    logger.info(f"Processing: {step_name}")
    
    if details:
        for key, value in details.items():
            logger.info(f"  {key}: {value}")


def log_output_file(logger, output_type, filepath, filesize=None):
    """
    Log output file creation.
    
    Parameters
    ----------
    logger : logging.Logger
        Logger instance
    output_type : str
        Type of output ('figure', 'processed_data', 'methods')
    filepath : str or Path
        Path to output file
    filesize : float, optional
        File size in MB
    """
    filepath = Path(filepath)
    
    logger.info(f"Created {output_type}: {filepath.name}")
    logger.debug(f"  Full path: {filepath}")
    
    if filesize:
        logger.debug(f"  Size: {filesize:.2f} MB")
    elif filepath.exists():
        size_mb = filepath.stat().st_size / (1024 * 1024)
        logger.debug(f"  Size: {size_mb:.2f} MB")


def log_validation(logger, validation_name, passed, details=None):
    """
    Log validation check results.
    
    Parameters
    ----------
    logger : logging.Logger
        Logger instance
    validation_name : str
        Name of validation check
    passed : bool
        Whether validation passed
    details : str, optional
        Additional details
    """
    status = "PASSED" if passed else "FAILED"
    level = logging.INFO if passed else logging.WARNING
    
    logger.log(level, f"Validation '{validation_name}': {status}")
    
    if details:
        logger.log(level, f"  {details}")


def log_completion(logger, start_time):
    """
    Log analysis completion with elapsed time.
    
    Parameters
    ----------
    logger : logging.Logger
        Logger instance
    start_time : datetime
        Start time of analysis
    """
    elapsed = datetime.now() - start_time
    elapsed_str = str(elapsed).split('.')[0]  # Remove microseconds
    
    logger.info("=" * 70)
    logger.info(f"Analysis completed successfully")
    logger.info(f"Total elapsed time: {elapsed_str}")
    logger.info("=" * 70)


def log_error(logger, error, context=None):
    """
    Log an error with context.
    
    Parameters
    ----------
    logger : logging.Logger
        Logger instance
    error : Exception
        The error that occurred
    context : str, optional
        Context about where/when error occurred
    """
    logger.error("=" * 70)
    logger.error("ERROR ENCOUNTERED")
    
    if context:
        logger.error(f"Context: {context}")
    
    logger.error(f"Error type: {type(error).__name__}")
    logger.error(f"Error message: {str(error)}")
    logger.error("=" * 70)
    
    # Log full traceback at debug level
    logger.debug("Full traceback:", exc_info=True)


# Example usage function
def get_example_usage():
    """Return example usage code as a string."""
    return """
# Example usage in a notebook:

from utils.logger import setup_logger, log_data_loading, log_processing_step, log_output_file, log_completion
from datetime import datetime

# Initialize logger
logger = setup_logger('figure_01')
start_time = datetime.now()

try:
    # Log data loading
    log_data_loading(logger, 'ERA5', '../era5/era5_*_Arctic.nc',
                    dims={'time': 552, 'lat': 120, 'lon': 720},
                    time_range=('1979-01', '2025-12'))
    
    # Log processing steps
    log_processing_step(logger, 'Calculating spatial trends',
                       details={'period': '1979-2014', 'method': 'linear regression'})
    
    # Log outputs
    log_output_file(logger, 'processed_data', 
                   'outputs/processed_data/figure_01/spatial_trends.nc')
    log_output_file(logger, 'figure', 
                   'outputs/figures/figure_01.png')
    
    # Log completion
    log_completion(logger, start_time)
    
except Exception as e:
    log_error(logger, e, context='During spatial trend calculation')
    raise
"""


if __name__ == "__main__":
    print(get_example_usage())
