import logging
import json
import time
from typing import Any, Callable
from functools import wraps

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module
        }
        if hasattr(record, "extra_info"):
            log_data.update(record.extra_info)
        return json.dumps(log_data)

def setup_logger():
    logger = logging.getLogger("LLMOpsLogger")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(JsonFormatter())
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logger()

def log_execution_time(func: Callable) -> Callable:
    """A decorator to log the execution time of agent functions."""
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"Function {func.__name__} completed successfully.", extra={"extra_info": {"execution_time_sec": round(execution_time, 4), "status": "success"}})
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"Function {func.__name__} failed: {str(e)}", extra={"extra_info": {"execution_time_sec": round(execution_time, 4), "status": "error", "error_type": type(e).__name__}})
            raise
    return wrapper
